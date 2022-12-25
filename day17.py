class Rock:
    types = [
        [
            [1,1,1,1]
        ],
        [
            [0,1,0],
            [1,1,1],
            [0,1,0]
        ],
        [
            [0,0,1],
            [0,0,1],
            [1,1,1]
        ],
        [
            [1],
            [1],
            [1],
            [1]
        ],
        [
            [1,1],
            [1,1]
        ]
    ]

    def __init__(self, x, y, type):
        self.type = type
        self.width = len(Rock.types[type][0])
        self.height = len(Rock.types[type])
        self.x = x
        self.y = y + self.height - 1
        self.build()

    def build(self):
        data = set()
        for y in range(self.height):
            for x in range(self.width):
                if Rock.types[self.type][y][x]:
                    data.add((self.x + x, self.y - y))
        self.data = data
                
    
    def wall_collision(self, wind) -> bool:
        # Check if wind (1 or -1) would push rock into wall
        new_x = self.x + wind
        if new_x == 0 or new_x + self.width - 1 == 8:
            return True
        else:
            return False

    def rock_collision(self, dx, dy, static_rocks):
        # Check if falling down 1 unit collides with a static rock or floor
        for (x,y) in self.data:
            if (x+dx,y+dy) in static_rocks or y+dy == 0:
                return True
        return False

    def sim(self, d, d_index, static_rocks: set):
        while True:
            # Wind phase
            wind = 1 if d[d_index] == ">" else -1
            if not self.wall_collision(wind) and not self.rock_collision(wind, 0, static_rocks):
                self.x += wind
                self.build()
            else:
                # Collision during wind phase means the rock simply doesn't move
                pass

            # Fall phase
            if not self.rock_collision(0, -1, static_rocks):
                self.y -= 1
                self.build()
            else:
                # Collision during fall phase makes this rock static in the environment and exits simulation
                static_rocks.update(self.data)
                return d_index+1

            d_index = (d_index + 1) % len(d)


def simulate(d):
    d_index = 0
    static_rocks = set()
    max_y = 0
    type = 0
    known_configs = dict()
    repeated_configs = 0
    for cntr in range(1000000):

        # print(f"Starting round {cntr}: current max y: {max_y}, rock type: {type}")

        rock = Rock(3, max_y + 4, type)
        d_index = rock.sim(d, d_index, static_rocks)    
        new_max_y = max(y for x,y in static_rocks)
        diff_y = new_max_y - max_y
        max_y += diff_y

        # print(f"  > Sim finished: type={type}, index={d_index}, diff={diff_y}")

        if (type, d_index, diff_y) not in known_configs:
            known_configs[type, d_index, diff_y] = cntr
            repeated_configs = 0
        else:
            repeated_configs += 1
            print(f"Round {cntr}: Found a repeated config from round {known_configs[type, d_index, diff_y]}: type={type}, index={d_index}, diff={diff_y}")

        if repeated_configs > 50:
            print(f"  !!! Config repeated 50 times in a row, exiting")
            break

        type = (type+1) % 5

    # TODO this is only for my input, needs to be generic
    start_increment = 0
    period_increment = 0
    period_start = 240
    period_end = 1979
    for (_,_,df), round in known_configs.items():
        if period_start <= round <= period_end:
            period_increment += df
        if round < period_start:
            start_increment += df
    print(f"period incr {period_increment}, start incr {start_increment}")

    period_len = period_end-period_start+1

    period_cnt = (1_000_000_000_000 - period_start) // period_len
    remain = (1_000_000_000_000 - period_start) % period_len

    remain_increment = 0
    for (_,_,df), round in known_configs.items():
        if period_start <= round <= period_start+remain-1:
            remain_increment += df

    print(f"period count {period_cnt}, remain {remain}")

    print(f"max_y: {start_increment + period_increment*period_cnt + remain_increment}")

def print_env(static_rocks, max_y, limit=None):
    ret = ""
    start = max_y+2-limit if limit != None else 1
    start = max(1, start) # Clamp
    for y in reversed(range(start, max_y+2)):
        ret += "|"
        for x in range(1,8):
            ret += "#" if (x, y) in static_rocks else "."
        ret += "|"
        ret += "\n"
    if start == 1:
        # Print floor too
        ret += "+-------+\n"
    print(ret)


d = open("17").read()
simulate(d)