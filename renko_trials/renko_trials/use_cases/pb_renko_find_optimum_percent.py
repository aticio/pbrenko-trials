from renko_trials.use_cases.pb_renko_create import PBRenkoCreateUseCase
from decimal import Decimal, getcontext


def find_optimum_percent(repo, symbol):
    found_percentages = []
    for i in (x / 10 for x in range(9, 101)):
        pb_renko_create_use_case = PBRenkoCreateUseCase(repo)
        pb_renko = pb_renko_create_use_case.create_pbrenko(symbol, i)

        if pb_renko.number_of_leaks == 0:
            found_percentages.append(i)

    if len(found_percentages) == 0:
        return None
    elif len(found_percentages) == 1:
        return found_percentages[0]
    else:
        getcontext().prec = 1
        for i, k in enumerate(found_percentages):
            all_equal = True
            for t, z in enumerate(found_percentages[i:]):
                if i + t != len(found_percentages) - 1:
                    if (float(Decimal(found_percentages[i + t + 1]) - Decimal(found_percentages[i + t]))) != float(0.1):
                        all_equal = False
                        break
            if all_equal:
                return k
