# This is a sample Python script.
import logging
import rankData
import strategy
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=RuntimeWarning)

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
FORMAT = '%(asctime)s : %(filename)s:%(lineno)d -  %(levelname)s :: %(message)s'
logging.basicConfig(filename="kite.log", format=FORMAT, level=logging.INFO)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    target = "US"
    if target == "US"   :
        startDate = "20250324"
    else:
        startDate = "20240205"

    try:
        # Gather data and rank them
        # ranking based on RDX
        rank = rankData.RankData(target, interval="1d")
        df = rank.load_data()
        rank.rank_data()

        # Strategy test
        # testStrategy = strategy.Strategy(target, capital="100000", max_positions=10, is_long=True)
        testStrategy = strategy.Strategy(target, capital="100000", max_positions=10, is_long=True)
        testStrategy.load_index()
        testStrategy.evaluate(start_date=startDate)

    except Exception as ex:
        print("Exception occurred.", ex)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
