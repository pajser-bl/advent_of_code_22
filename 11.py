from datetime import datetime

monkey_input = """Monkey 0:
  Starting items: 72, 64, 51, 57, 93, 97, 68
  Operation: new = old * 19
  Test: divisible by 17
    If true: throw to monkey 4
    If false: throw to monkey 7

Monkey 1:
  Starting items: 62
  Operation: new = old * 11
  Test: divisible by 3
    If true: throw to monkey 3
    If false: throw to monkey 2

Monkey 2:
  Starting items: 57, 94, 69, 79, 72
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 0
    If false: throw to monkey 4

Monkey 3:
  Starting items: 80, 64, 92, 93, 64, 56
  Operation: new = old + 5
  Test: divisible by 7
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 4:
  Starting items: 70, 88, 95, 99, 78, 72, 65, 94
  Operation: new = old + 7
  Test: divisible by 2
    If true: throw to monkey 7
    If false: throw to monkey 5

Monkey 5:
  Starting items: 57, 95, 81, 61
  Operation: new = old * old
  Test: divisible by 5
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 6:
  Starting items: 79, 99
  Operation: new = old + 2
  Test: divisible by 11
    If true: throw to monkey 3
    If false: throw to monkey 1

Monkey 7:
  Starting items: 68, 98, 62
  Operation: new = old + 3
  Test: divisible by 13
    If true: throw to monkey 5
    If false: throw to monkey 6"""

test_monkey_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

round_num = 0


class Monkey:
    def __init__(self, index, items, operation, test, true, false):
        self.index = index
        self.items: list = items
        self.operation: tuple = operation
        self.test = test
        self.true = true
        self.false = false

        self.inspections = 0

    def add_item(self, item):
        self.items.append(item)

    def action(self, _monkeys, modulus = 1):
        while self.items:
            self.inspections += 1
            item = self.items.pop(0)
            if self.operation[0] == 'mul':
                item = item * self.operation[1]
            if self.operation[0] == 'add':
                item = item + self.operation[1]
            if self.operation[0] == 'sqr':
                item = item * item
            # item = item // 3
            item = item % modulus
            if item % self.test == 0:
                _monkeys[self.true].add_item(item)
            else:
                _monkeys[self.false].add_item(item)

    @classmethod
    def from_raw_input(cls, raw_monkey):
        raw_index, raw_items, raw_op, raw_test, raw_true, raw_false = raw_monkey.split('\n')

        def parse_op(raw_op: str):
            raw_op = raw_op.replace(' ', '').replace('Operation:new=', '')
            if raw_op.startswith('old*old'):
                return 'sqr', None
            elif raw_op.startswith('old*'):
                return 'mul', int(raw_op.replace('old*', ''))
            elif raw_op.startswith('old+'):
                return 'add', int(raw_op.replace('old+', ''))

        return cls(
            index=int(raw_index.split()[1].replace(':', '')),
            items=[int(item) for item in raw_items.replace('Starting items: ', '').split(',')],
            operation=parse_op(raw_op),
            test=int(raw_test.replace('Test: divisible by ', '')),
            true=int(raw_true.replace('If true: throw to monkey ', '')),
            false=int(raw_false.replace('If false: throw to monkey ', ''))
        )


# monkey_input = test_monkey_input.split('\n\n')
monkey_input = monkey_input.split('\n\n')
mudulus = 1
monkeys = [Monkey.from_raw_input(raw_monkey) for raw_monkey in monkey_input]
for monkey in monkeys:
    mudulus *= monkey.test
# for i in range(20):
for i in range(10000):
    start = datetime.now()
    round_num += 1
    for monkey in monkeys:
        monkey.action(monkeys, mudulus)
    print(f'Round {round_num} elapsed in {datetime.now() - start}')

insp = []
for monkey in monkeys:
    insp.append(monkey.inspections)
print(sorted(insp, reverse=True)[0]*sorted(insp, reverse=True)[1])
