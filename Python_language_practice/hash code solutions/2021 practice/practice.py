from functools import reduce
from itertools import combinations
from sys import argv
from time import time


def write_deliveries(output_file, deliveries):
    with open(output_file, 'w') as g:
        g.write(str(len(deliveries)) + '\n')
        for delivery in deliveries:
            g.write(' '.join(str(i) for i in delivery) + '\n')


def score_pizzas(pizzas, ids):
    return len(reduce(lambda a, b: a | b, [pizzas[id_new] for id_new in ids[1:]])) ** 2


def optimize(output_file, deliveries, pizzas, score):
    write_deliveries(output_file, deliveries)
    best = [deliveries, score]
    frontier = [[deliveries, score]]
    iterators = [0]
    for deli, state_score in frontier:
        original_scores = {x: score_pizzas(pizzas, deli[x]) for x in range(len(deli))}
        changes = []
        changed = set()
        for x1, x2 in combinations(range(len(deli)), 2):
            iterators[0] += 1
            if x1 in changed or x2 in changed:
                continue
            d1 = deli[x1]
            d2 = deli[x2]
            best_improve = [0, -1, -1, -1, -1]
            for a in d1[1:]:
                for b in d2[1:]:
                    dd1 = [d for d in d1 if d != a] + [b]
                    dd2 = [d for d in d2 if d != b] + [a]
                    ds1 = score_pizzas(pizzas, dd1)
                    ds2 = score_pizzas(pizzas, dd2)
                    imp_score = ds1 + ds2 - original_scores[x1] - original_scores[x2]
                    if imp_score > best_improve[0]:
                        best_improve = [imp_score, x1, x2, a, b]
            if best_improve[0] > 1:
                changes.append(best_improve[1:])
                changed.add(best_improve[1])
                changed.add(best_improve[2])
        if changes:
            for x1, x2, a, b in changes:
                deli[x1] = [deli[x1][0]] + [d for d in deli[x1][1:] if d != a] + [b]
                deli[x2] = [deli[x2][0]] + [d for d in deli[x2][1:] if d != b] + [a]
            de_score = sum(score_pizzas(pizzas, delivery) for delivery in deli)
            if de_score > best[1]:
                print(f'Optimized to {de_score} from {best[1]}')
                print(f'Frontier size: {len(frontier)}. Made {len(changes)} changes, '
                      f'from a delivery size of: {len(deliveries)} after {iterators[0]} inner iterations.')
                best = [deli, de_score]
                frontier.append([deli, de_score])
                write_deliveries(output_file, deli)
    return best


def find_delivery(remaining, big_first, start):
    matrices = 10 ** 4
    best_deliveries = []
    best_score = 0
    for i, c in enumerate(combinations([bf for bf in big_first if bf[0] in remaining], sum(start))):
        if i == matrices:
            break
        deliveries = []
        score = 0
        for s in start:
            delivery = c[sum([len(d) for d in deliveries]):sum([len(d) for d in deliveries]) + s]
            deliveries.append([d[0] for d in delivery])
            score += len(reduce(lambda a, b: a | b, [entry[1] for entry in delivery])) ** 2
        if score > best_score:
            best_score = score
            best_deliveries = deliveries
    return best_deliveries, best_score


def solve(output_file, m, t2, t3, t4, pizzas):
    deliveries = []
    big_first = sorted([(x, pizzas[x]) for x in range(m)], key=lambda found: -len(found[1]))
    remaining = {x for x in range(m)}
    score = 0
    iterators = 0
    while t4 > 2 and len(remaining) > 11:
        if t4 % 100 == 0:
            print(t4, t3, t2, len(remaining), score)
        delivery = []
        ingredients = set()
        while len(delivery) < 4:
            best = [set(), -1]
            for x, pizza in big_first:
                if x not in remaining or x in delivery:
                    continue
                union = pizza | ingredients
                if len(union) > len(best[0]):
                    best = [union, x]
            ingredients = best[0]
            delivery.append(best[1])
        deliveries.append([4] + delivery)
        remaining -= set(delivery)
        t4 -= 1
        score += len(ingredients) ** 2
        big_first = [bf for bf in big_first if bf[0] in remaining]
    while t3 > 2 and len(remaining) > 8:
        if t3 % 100 < 3:
            print(t4, t3, t2, len(remaining), score)
        delivery = []
        ingredients = set()
        while len(delivery) < 3:
            best = [set(), -1]
            for x, pizza in big_first:
                if x not in remaining or x in delivery:
                    continue
                union = pizza | ingredients
                if len(union) > len(best[0]):
                    best = [union, x]
            ingredients = best[0]
            delivery.append(best[1])
        deliveries.append([3] + delivery)
        remaining -= set(delivery)
        t3 -= 1
        score += len(ingredients) ** 2
    while True:
        iterators += 1
        if iterators % 100 == 0:
            print(f'remaining: {len(remaining)} t4: {t4} t3: {t3} t2: {t2}')
        if t4 > 25:
            delivery, value = find_delivery(remaining, big_first, [4] * 20)
            score += value
            for d in delivery:
                remaining -= set(d)
                deliveries.append([len(d)] + d)
            t4 -= 20
            continue
        elif t4 == 0 and t3 > 25:
            delivery, value = find_delivery(remaining, big_first, [3] * 20)
            score += value
            for d in delivery:
                remaining -= set(d)
                deliveries.append([len(d)] + d)
            t3 -= 20
            continue
        elif t4 == 0 and t3 == 0 and t2 > 25:
            delivery, value = find_delivery(remaining, big_first, [2] * 20)
            score += value
            for d in delivery:
                remaining -= set(d)
                deliveries.append([len(d)] + d)
            t2 -= 20
            continue
        start = [4] * min(2, t4) + [3] * min(2, t3) + [2] * min(2, t2)
        if len(start) < 2:
            if len(start) == 1:
                if sum(start) <= len(remaining):
                    delivery, value = find_delivery(remaining, big_first, start)
                    score += value
            return optimize(output_file, deliveries, pizzas, score)
        best_deliveries = None
        best_score = 0
        seen = set()
        for pair in combinations(start, 2):
            if pair in seen:
                continue
            if sum(pair) <= len(remaining):
                delivery, value = find_delivery(remaining, big_first, pair)
                if value > best_score:
                    best_deliveries = delivery
                    best_score = value
                seen.add(pair)
        if not best_score:
            return optimize(output_file, deliveries, pizzas, score)
        score += best_score
        for delivery in best_deliveries:
            remaining -= set(delivery)
            deliveries.append([len(delivery)] + delivery)
            if len(delivery) == 4:
                t4 -= 1
            elif len(delivery) == 3:
                t3 -= 1
            else:
                t2 -= 1


def main():
    input_files = {
        'a': 'a_example',
        'b': 'b_little_bit_of_everything.in',
        'c': 'c_many_ingredients.in',
        'd': 'd_many_pizzas.in',
        'e': 'e_many_teams.in'
    }
    to_run = []
    if len(argv) > 2:
        print('This script only takes one optional parameter. Run either parameterless, or with one parameter, '
              'containing the letter codes for the input files you wish to process!')
        return
    if len(argv) == 2:
        if any(c not in 'abcde' for c in argv[1]):
            print('Illegal option', argv[1])
            return
        for c in set(argv[1]):
            to_run.append(input_files[c])
    else:
        to_run += list(input_files.values())
    to_run.sort()
    print('Going to run:')
    print('\n'.join(to_run))
    for file in to_run:
        t = time()
        output_file = (file[:file.find('.')] if '.' in file else file) + '.out'
        with open(file) as f:
            m, t2, t3, t4 = map(int, f.readline().split())
            pizzas = []
            for _ in range(m):
                pizza = f.readline().split()
                pizzas.append(set(pizza[1:]))
            deliveries, score = solve(output_file, m, t2, t3, t4, pizzas)
            print(f'Finished {file} with score {score} in {time() - t} seconds.')
            write_deliveries(output_file, deliveries)


if __name__ == '__main__':
    main()
