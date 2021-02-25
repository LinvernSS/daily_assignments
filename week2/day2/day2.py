import pandas as pd


# Lucas Invernizzi Week 2 Day 2 Assignment

def format_strings(d, col_name):
    d[col_name] = d[col_name].str.title()
    return d


def q1(d):
    print('Question 1')
    print(d.head())


def q2(d):
    print('\nQuestion 2')
    d.info()


def q3(d):
    print('\nQuestion 3')
    avg_pay = round(d['BasePay'][0:10000].mean(), 2)
    print('Average base pay for first 10000 Employees: ${}'.format(f'{avg_pay:,}'))


def q4(d):
    print('\nQuestion 4')
    max_pay = round(d['TotalPayBenefits'].max(), 2)
    print('Maximum of all total pay benefits: ${}'.format(f'{max_pay:,}'))


def q5(d):
    print('\nQuestion 5')
    employee_mask = d['EmployeeName'] == 'Joseph Driscoll'
    title = data[employee_mask]['JobTitle'].iloc[0]
    print('Joseph Driscoll\'s title is: {}'.format(title))


def q6(d):
    print('\nQuestion 6')
    employee_mask = d['EmployeeName'] == 'Joseph Driscoll'
    total_pay = round(data[employee_mask]['TotalPayBenefits'].iloc[0], 2)
    print('Joseph Driscoll\'s total pay with benefits is: ${}'.format(f'{total_pay:,}'))


def q7(d):
    print('\nQuestion 7')
    max_pay = d['TotalPayBenefits'].max()
    pay_mask = d['TotalPayBenefits'] == max_pay
    max_name = d[pay_mask]['EmployeeName'].iloc[0]
    print('The person with the highest pay is: {} at ${}'.format(max_name, f'{max_pay:,}'))


def q8(d):
    print('\nQuestion 8')
    min_pay = d['TotalPayBenefits'].min()
    pay_mask = d['TotalPayBenefits'] == min_pay
    min_name = d[pay_mask]['EmployeeName'].iloc[0]
    print('The person with the lowest pay is: {} at ${}'.format(min_name, f'{min_pay:,}'))
    print('It is odd that they have a negative pay.')


def q9(d):
    print('\nQuestion 9')
    for i in range(2011, 2015):
        year_mask = d['Year'] == i
        avg_pay = round(d[year_mask]['TotalPay'].mean(), 2)
        print('Average pay for all employees in {}: ${}'.format(i, f'{avg_pay:,}'))


def q10(d):
    print('\nQuestion 10')
    titles = pd.unique(d['JobTitle'])
    print('Number of unique job titles: {}'.format(len(titles)))


def q11(d):
    print('\nQuestion 11')
    counts = d['JobTitle'].value_counts()
    print('Top 7 most common job titles:')
    for i, job in zip(range(1, 8), list(counts.iloc[0:7].index)):
        print('Number {}: {}'.format(i, job))


def q12(d):
    print('\nQuestion 12')
    year_mask = d['Year'] == 2013
    counts = d[year_mask]['JobTitle'].value_counts()
    one_title_mask = counts == 1
    num_titles = len(counts[one_title_mask])
    print('Number of job titles in 2013 with only one holder: {}'.format(num_titles))


def q13(d):
    print('\nQuestion 13')
    count = d['JobTitle'].str.contains('Chief').sum()
    print('Number of people with Chief in their title: {}'.format(count))


def q14(d):
    print('\nQuestion 14')
    title_len = d['JobTitle'].str.len()
    corr = round(title_len.corr(d['TotalPayBenefits'], method='pearson'), 5)
    print('Pearson correlation coefficient between job title length and pay is: {}'.format(corr))
    print('This shows no correlation.')


if __name__ == "__main__":
    data = pd.read_csv('Salaries.csv')
    data = format_strings(data, 'EmployeeName')
    data = format_strings(data, 'JobTitle')
    q1(data)
    q2(data)
    q3(data)
    q4(data)
    q5(data)
    q6(data)
    q7(data)
    q8(data)
    q9(data)
    q10(data)
    q11(data)
    q12(data)
    q13(data)
    q14(data)
