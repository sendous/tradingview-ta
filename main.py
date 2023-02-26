import csv
import tradingview_ta as ta



with open('coins.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        symbol = row[0].strip()
        try:
            handler_day = ta.TA_Handler(
                symbol=symbol,
                screener="crypto",
                exchange='BINANCE',
                interval=ta.Interval.INTERVAL_1_DAY
            )
            handler_4H = ta.TA_Handler(
                symbol=symbol,
                screener='crypto',
                exchange='BINANCE',
                interval=ta.Interval.INTERVAL_4_HOURS
            )
            handler_1H = ta.TA_Handler(
                symbol=symbol,
                screener='crypto',
                exchange='BINANCE',
                interval=ta.Interval.INTERVAL_1_HOUR
            )
            handler_15min = ta.TA_Handler(
                symbol=symbol,
                screener='crypto',
                exchange='BINANCE',
                interval=ta.Interval.INTERVAL_15_MINUTES
            )
            handler_1min = ta.TA_Handler(
                symbol=symbol,
                screener='crypto',
                exchange='BINANCE',
                interval=ta.Interval.INTERVAL_1_MINUTE
            )
            analysis_day = handler_day.get_analysis().summary
            analysis_4H = handler_4H.get_analysis().summary
            analysis_1H = handler_1H.get_analysis().summary
            analysis_15min = handler_15min.get_analysis().summary
            analysis_1min = handler_1min.get_analysis().summary
            if analysis_day['RECOMMENDATION'] == 'BUY':
                print(f'{analysis_1min}','\n', f'{analysis_15min}')
                print(f'{analysis_1H}')
                print(f'{analysis_4H}')
                print(f'{analysis_day} : {symbol}')
                print('\n')
        except:
            pass