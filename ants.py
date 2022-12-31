def generate_scenarios(initial_situation, i=0):
    if i == len(initial_situation):
        return [initial_situation]

    scenario1 = [(element[0], element[1]) if isinstance(element, tuple) else element for element in initial_situation]
    scenario1[i] = (scenario1[i], 1)
    scenario2 = [(element[0], element[1]) if isinstance(element, tuple) else element for element in initial_situation]
    scenario2[i] = (scenario2[i], -1)
    return generate_scenarios(scenario1, i=i+1) + generate_scenarios(scenario2, i=i+1)


def simulate(scene, l):
    if len(scene) == 0:
        return 0

    step(scene, l)
    return 1 + simulate(scene, l)


def step(scene, l):
    fell = []
    extra_handled = []
    for i in range(len(scene)):
        if i in extra_handled:
            continue
        ant_position, direction = scene[i]
        if direction == -1 and ant_position == 1:
            fell.append(i)
        elif direction == 1 and ant_position == l:
            fell.append(i)
        else:
            ant_one_further, idx_ant_one_further = get_ant(scene, ant_position + direction)
            ant_two_further, idx_ant_two_further = get_ant(scene, ant_position + 2 * direction)
            if ant_one_further is not None:
                if ant_one_further[1] * direction == -1:
                    scene[i] = (scene[i][0], direction * -1)
                    scene[idx_ant_one_further] = (scene[idx_ant_one_further][0], scene[idx_ant_one_further][1] * -1)
                else:
                    scene[i] = (scene[i][0] + direction, direction)
            elif ant_two_further is not None:
                if ant_two_further[1] * direction == -1:
                    scene[i] = (scene[i][0], direction * -1)
                    scene[idx_ant_two_further] = (scene[idx_ant_two_further][0], scene[idx_ant_two_further][1] * -1)
                else:
                    scene[i] = (scene[i][0] + direction, direction)
            else:
                scene[i] = (scene[i][0] + direction, direction)
    for i in range(len(fell)):
        scene.pop(fell[i] - i)


def get_ant(scene, ant_position):
    for i in range(len(scene)):
        if scene[i][0] == ant_position:
            return scene[i], i
    return None, None


n_test_cases = int(input())

for _ in range(n_test_cases):
    t = input().split()
    l, n = int(t[0]), int(t[1])
    ants = []
    while len(ants) < n:
        ants += [int(c) for c in input().split()]

    scenarios = generate_scenarios(ants)
    times = []
    for scenario in scenarios:
        times.append(simulate(scenario, l) - 1)
    print(min(times), max(times))
