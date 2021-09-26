import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            while value != 0:
                self.contents.append(str(key))
                value = value - 1

    def draw(self, number_of_balls):
        drawn_balls = []
        if len(self.contents) >= number_of_balls:
            while number_of_balls != 0:
                random_ball = random.choice(self.contents)
                drawn_balls.append(random_ball)
                self.contents.remove(random_ball)
                number_of_balls += -1
            else:
                drawn_balls = self.contents
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    box = hat.contents
    expected_colors = []
    experiments = num_experiments
    for key, value in expected_balls.items():
        expected_colors.append(key)

    if len(box) >= num_balls_drawn:
        passed_experiments = 0
        while experiments != 0:
            random_letters = copy.deepcopy(expected_colors)
            while num_balls_drawn != 0:
                rand = random.choice(box)
                random_letters.append(rand)
                box.remove(rand)
                num_balls_drawn += - 1
            check_list = [expected_colors[n] for n in range(len(expected_colors))
                          if random_letters.count(expected_colors[n]) == (expected_balls[expected_colors[n]] + 1)]
            if len(check_list) == len(expected_balls):
                passed_experiments += 1
                print(f"check list {check_list}")

            experiments = experiments - 1
        return passed_experiments / num_experiments
    else:
        return hat.contents




