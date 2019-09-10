import glob, os, calendar
# os.chdir("_posts")

# for file in glob.glob("*"):
    # print(file)

mylist = os.listdir(path='_posts')
# print(mylist)

try:
    os.makedirs("get2016")
except FileExistsError:
    # directory already exists
    pass

years_arr = []
# months = []
# days = []
# y=""
for file in mylist:
    y = file[0:4]
    m = file[6:7]
    d = file[9:10]

    if int(m) >= 1:
        m2 = "0" + m
        # print(m2)

    if int(d) >= 1:
        d2 = "0" + d
        # print(d)

    years = '{}'.format(y)
    months = '{}/{}'.format(y, m2)
    days = '{}/{}/{}'.format(y, m2, d2)
    # print(years)
    # print(months)

    try:
        os.makedirs(years)
    except FileExistsError:
        # directory already exists
        pass

    try:
        os.makedirs(months)
    except FileExistsError:
        # directory already exists
        pass

    try:
        os.makedirs(days)
    except FileExistsError:
        # directory already exists
        pass

    year_file = years + "/index.html"
    # print(year_file)
    month_file = months + "/index.html"
    print(month_file)
    day_file = days + "/index.html"
    print(day_file)

    yaml_open = "---"
    layout = "layout: year"
    permalink = 'permalink: "' + years + '"'
    # permalink = "permalink: " + years
    redirect = "redirect_from: archive/" + years
    title = 'title: ' + years
    year = "year: " + years
    yaml_close = "---"
    content = "This is a test"
    lines = '{}\n{}\n{}\n{}\n{}\n{}\n{}\n\n{}\n'.format(yaml_open, layout, permalink, redirect, title, year, yaml_close, content)

    yf = open(year_file, 'w+')
    yf.write(lines)
    yf.close()

    yaml_open = "---"
    layout = "layout: month"
    permalink = 'permalink: ' + months
    redirect = "redirect_from: archive/" + months
    title = "title: Archive for " + months
    year = "year: " + years
    month = "month: " + '"' + m2 + '"'
    yaml_close = "---"
    content = "This is a test"
    lines = '{}\n{}\n{}\n{}\n{}\n{}\n{}\n\n{}\n'.format(yaml_open, layout, permalink, redirect, title, year, month, yaml_close, content)

    mf = open(month_file, 'w+')
    mf.write(lines)
    mf.close()

#     x = months
#     line1 = "---"
#     line2 = "layout: default"
#     line3 = "permalink: " + months
#     # line3 = "permalink: " + years
#     line4 = "redirect_from: archive/" + months
#     line5 = "title: Month " + months
#     line6 = "---"
#     line7 = "\nThis is a test"
#     lines = '{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7)

#     # mf = open('month_file', 'w+')
#     # mf.write(lines)
#     # mf.close()

#     # df = open('day_file', 'w+')
#     # df.write("Fuck")
#     # df.close()

#     # print(date)
#     # print(year_file)
#     # print(month_file)
#     # print(day_file)

#     # f = open(year_file, 'w+')
#     # f.write(lines)
#     # f.close()

#     yf = open(year_file, 'w+')
#     yf.write(ylines)
#     yf.close()

#     mf = open(month_file, 'w+')
#     mf.write(lines)
#     mf.close()

#     # f = open('year_file', 'w+')
#     # f.write("Fuck")
#     # f.close()


#     # if int(m) >= 1 and int(m) < 10:
#     #     m2 = str("0" + m)
#     # if int(d) >= 1 and int(d) < 10:
#     #     d2 = str("0" + d)

#     # date = '{}/{}/{}'.format(y, m2, d2)
#     # filename = "_site/" + date + "/index.html"
#     # # print(date)
#     # print(filename)

#     # line1 = "---"
#     # line2 = "layout: archive"
#     # line3 = "permalink: " + date
#     # line4 = "redirect_from: 'archive/" + date
#     # line5 = "title: Month " + y
#     # line6 = "---"

#     # f = open('filename', 'w+')
#     # f.write("Fuck")
#     # f.close()

# #     if y not in years:
# #         years.append(y)
# #         # print(years)
# # print(len(years))
# # for x in range(len(years)):
# #     print(years[x])
# #     m = file[6:7]
# #     print(m)
# #     years[x] = m
#     # print(years)
#     # if int(m) >= 1 and int(m) < 10:
#     #     m2 = str("0" + m)

#     # print(m2)
#     # years.append(m2)
#     # print(years)
#     # years[m].append(m1)

# # print(years)

#         # if int(m) >= 1 and int(m) < 10:
#         #     m2 = str("0" + m)

# #         for d in m:
# #             d = file[9:10]

# #             if int(d) > 0 and int(d) < 10:
# #                 d2 = str("0" + d)

# #                 print(y, m2, d2)

# #                 year_file = "/_site/" + y + "/index.html"
# #                 month_file = "/_site/" + y + "/" + m2 + "/index.html"
# #                 day_file = "/_site/" + y + "/" + m2 + "/" + d2 + "/index.html"

# #     print('{}\n{}\n{}\n'.format(year_file, month_file, day_file))

# #     line1 = "---"
# #     line2 = "layout: archive"
# #     line3 = "permalink: " + y + ""
# #     line4 = "redirect_from: archive/" + y
# #     line5 = "title: " + m + " " + y + ""
# #     line6 = "---"
# #     lines = '{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6)

# #     with open(year_file, 'w+') as f:
# #         f.write(lines)
# #         f.close()

# #     with open(month_file, 'w+') as f:
# #         f.write(lines)
# #         f.close()

# #     # with open(day_name, 'w+') as f:
# #     #     f.write(lines)
# #     #     f.close()

# # print(years, months, days)

#     # month = calendar.month_name[int(m)]
#     # if int(m) > 0 and int(m) < 10:
#     #     m2 = str("0" + m)
#     # print(m2)
#     # year_filename = "/_site/" + y + "/index.html"
#     # month_filename = "/_site/" + y + "/" + m2 + "/index.html"
#     # day_filename = "/_site/" + m2 + "/" + d + "/index.html"

#     # line1 = "---"
#     # line2 = "layout: archive"
#     # line3 = "permalink: " + y + ""
#     # line4 = "redirect_from: archive/" + y
#     # line5 = "title: " + month + " " + y + ""
#     # line6 = "---"
#     # lines = '{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6)

#     # with open(year_filename, 'w+') as f:
#     #     f.write(lines)
#     #     f.close()

#     # with open(month_filename, 'w+') as f:
#     #     f.write(lines)
#     #     f.close()

#     # # with open(day_filename, 'w+') as f:
#     # #     f.write(lines)
#     # #     f.close()


#     # print(y, m, d)

