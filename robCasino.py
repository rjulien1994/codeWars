state = None
def pseudorandom():
    global state, random_seed
    if state is None:
        # initialize RNG with seed
        state = (random_seed & 0x1FF) + 1
    # determine next pseudorandom number
    state ^= state >> 6
    state ^= state << 4
    state &= 0x1FF
    state ^= state >> 5
    return state

def reel(position):
    # return the 3 symbols on the reel strip around this position that would be seen on machine
    reel_strip = ('#', '', '$', '', '%', '', '&', '')
    return [reel_strip[(position + row) % len(reel_strip)] for row in (-1, 0, 1)]

def spin():
    # spin each reel and return a 2D array of the symbols that landed
    random = pseudorandom()
    stop3 = random & 0x7
    random >>= 3
    stop2 = random & 0x7
    random >>= 3
    stop1 = random & 0x7
    return [reel(stop1), reel(stop2), reel(stop3)]

def evaluate(view):
    # determine the payout based on the 2D array of symbols in view
    payline = [column[1] for column in view]
    for symbol in payline:
        count = payline.count(symbol)
        if count > 1:
            paytable = {
                3: {'$': 100, '#': 50, '&': 25, '%': 20, '': 0},
                2: {'$': 5, '#': 3.5, '&': 2.75, '%': 2.5, '': 0}
            }
            return paytable[count][symbol]
    if all(payline):
        return 0.5  # consolation prize for mismatched symbols
    return 0

def play(wager):
    # stake a bet at the given wager amount to play the game
    global bankroll, threshold
    assert type(wager) is int and 0 < wager <= bankroll
    view = spin()
    g = (-1 + evaluate(view))
    bankroll +=  g * wager  # cost to play and award
    if bankroll < 1.00 or bankroll >= threshold:
        raise FutureWarning  # end the session
    return view, bankroll

def test():
    global bankroll, threshold, random_seed
    bankroll = 20.00  # set initial funds
    threshold = 1_000_000.00  # set goal
    random_seed = 0  # set seed for RNG
    try:
        session(play)
    except AssertionError:
        test.fail('Assertion error. Bad wager?')
        raise
    except FutureWarning:
        pass
    finally:
        return (bankroll >= threshold, 'Remainig funds: ' + str(bankroll))

def session(play):
    symbols = ['#', '', '$', '', '%', '', '&', '']
    viewToNum = [[symbols[i-1], symbols[i], symbols[(i+1)%8]] for i in range(8)]
    
    view, wallet = play(1)

    nextState = 0
    for s in range(len(view)):
        nextState |= viewToNum.index(view[s]) << 3*(2-s)
    
    while True:
        nextState ^= nextState >> 6
        nextState ^= nextState << 4
        nextState &= 0x1FF
        nextState ^= nextState >> 5

        nextView = [nextState >> n & 0x7 for n in range(0,9,3)]
        bet = 1

        for i in range(0,8,2):
            if nextView.count(i) > 1:
                bet = int(wallet - wallet%1)
                break
        view, wallet = play(bet)
        

test()
