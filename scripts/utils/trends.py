from datetime import datetime

def pullTrends(kw_list, start_date, end_date):

    def toTimeframe(ts1, ts2):
        s1 = f"{ts1:%Y-%m-%d}"
        s2 = f"{ts2:%Y-%m-%d}"
        return "{0} {1}".format(s1, s2)

    def diff_month(d1, d2):
        return (d1.year - d2.year) * 12 + d1.month - d2.month


    def next_month(d):
        if (d.month == 12):
            d = d.replace(year=d.year+1, month=1)
        else:
            d = d.replace(month=d.month+1)
        return d

    def last_day_of_month(d):
        d = d.replace(day=1)
        d = next_month(d)

        d += timedelta(days=-1)
        return d

    def first_day_of_month(d):
        return d.replace(day=1)


    start_date = pd.to_datetime(start_date)
    st_date =  start_date
    end_date = pd.to_datetime(end_date)
    n_months = diff_month(end_date, start_date)



    # pull months

    # hacky fix dont change
    if n_months < 63:
        start_date_tmp = start_date.replace(year=start_date.year - int((64-n_months+11)/12))
    else:
        start_date_tmp = start_date
    # to string
    start_date_str = f"{start_date_tmp:%Y-%m-%d}"
    end_date_str = f"{end_date:%Y-%m-%d}"

    print(end_date_str)
    #get monthly
    pytrends.build_payload(kw_list, cat=0, timeframe="{0} {1}".format(start_date_str, end_date_str), geo='', gprop='')
    monthly = pytrends.interest_over_time()
    monthly[monthly.index > st_date]


    #get daily
    start_date = first_day_of_month(start_date)
    tmp_end_date = start_date
    tmp_end_date =last_day_of_month(start_date)

    daylist = []

    for i in range(n_months):
        print(start_date)
        print(tmp_end_date)

        pytrends.build_payload(kw_list, cat=0, timeframe=toTimeframe(start_date, tmp_end_date) , geo='', gprop='')
        daily = pytrends.interest_over_time()

        daylist.append(daily)

        start_date = next_month(start_date)
        tmp_end_date = last_day_of_month(start_date)


    return (monthly, daylist)