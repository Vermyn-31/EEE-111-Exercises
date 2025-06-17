fish_dict = {}

class Fish:
    def __init__(self, size, name):
        self.size = int(size)
        self.name = name
    
    def eat_fish(self, other_fish):
          # TODO: Add method that simulates this fish
        #       trying to feed other_fish
        #
        #       This method returns the "winning" `Fish`
        if self.size > other_fish.size:
            self.size += other_fish.size
            fish_dict[self.name] = self.size
            del fish_dict[other_fish.name]

            return self
            
        other_fish.size += self.size
        fish_dict[other_fish.name] = other_fish.size
        del fish_dict[self.name]

        return other_fish


    def feed(self, pellet_size):
          # TODO: Add method that simulates this fish
        #       feeding on a pellet of size pellet_size
        #
        #       This method returns nothing (i.e. None)
        self.size  += pellet_size
        fish_dict[self.name] = self.size


def main():
    global fish_dict
    t = int(input())
    for i in range(t):
        n_fishes, n_evt = [int(x) for x in input().split()]

        for _ in range(n_fishes):
            name_f, size_f = input().split(maxsplit=1)
            fish_dict[name_f] = int(size_f)
            # TODO: process each fish with initial sizes

        for _ in range(n_evt):
            evt, evt_args = input().split(maxsplit=1)
            #evt = evt.strip()
            if evt == "eat":
                f1, f2 = evt_args.split(" ")
                
                for each_fish in fish_dict.items():
                    f_size, f_name = each_fish[1],each_fish[0]
                    if f1 == f_name:
                        fish_1 = Fish(int(f_size), f_name)
                    if f2 == f_name:
                        fish_2 = Fish(int(f_size), f_name)

                winner = fish_1.eat_fish(fish_2)
                    
            elif evt == "feed":
                f, pellet = evt_args.split(" ")

                for each_fish in fish_dict.items():
                    f_size, f_name = each_fish[1],each_fish[0]
                    if f == f_name:
                        fish = Fish(f_size, f_name)
                    
                fish.feed(int(pellet))
                    
            
            # TODO: Process feeding events
        
        # TODO: Print remaining fishes and fishes sorted in
        #       decreasing size
        #
        # HINT: Use `sorted()` with a `key` argument.


        print(f"Case #{i+1}: Remaining fish(es): {len(fish_dict)}")
        sorting_fish_dict = {}
        for f_name,f_size in fish_dict.items():
            if f_size not in sorting_fish_dict:
                sorting_fish_dict[f_size] = []
            sorting_fish_dict[f_size].append(f_name)

        for f_name in sorted(sorting_fish_dict, reverse=True):
            for f_size in sorted(sorting_fish_dict[f_name]):
                print(f_size,f_name)
                fish_dict.clear()
            

if __name__ == '__main__':
    main()