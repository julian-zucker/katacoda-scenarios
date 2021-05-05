I've written tons of functions to process data files. Some of the time, the
data is already formatted well; at other times, I want to modify the columns.
I often do this by writing some huge Python script. But when I want to do it
right, I use a higher-order function to simplify the process.

Suppose we have these dictionaries:

```
data = [
    {
        "name": "",
        "age": 35,
        "salary": 100000,
    },
    {
        "name": "Jane Doe",
        "age": 42,
        "salary": 150000,
    },
    {
        "name": "John Doe",
        "age": "23",
        "salary": 100000,
    },
    {
        "name": "Foo Bar",
        "age": "302",
        "salary": "123456",
    },
    {
        "name": "Bar Foo",
        "age": "30",
        "salary": "123",
    },
]
```{{execute windows}}


And there are a few operations we want to do to filter and clean the
data:
    * Ignore any person with an empty name.
    * Ignore any person with an age over 100.
    * Make sure ages are numbers, not strings.
    * Make sure salaries are numbers, not strings.
    * Convert salaries which are less than $1,000 from hourly rates to yearly.

That's a lot of tasks, and doing them for each element will get pretty difficult
to follow. Let's start by writing functions that can do each of those things
one at a time, and then work on combining them with a higher-order function.

Ignore any person with an empty name:
```
def has_empty_name(person):
    return person['name'] == ''

```{{execute windows}}

Ignore any person with an age over 100:
```
def has_age_over_100(person):
    return person['age'] > 100

```{{execute windows}}

Make sure ages are numbers, not strings:
```
def convert_age_to_number(person):
    person['age'] = float(person['age'])

```{{execute windows}}

Make sure salaries are numbers, not strings:
```
def convert_salary_to_number(person):
    person['salary'] = float(person['salary'])

```{{execute windows}}

Convert salaries which are less than $1,000 from hourly rates to yearly:
```
def convert_salary_to_yearly(person):
    if person['salary'] < 1000:
        # 2000 work hours in the year, roughly
        person['salary'] = 2000 * person['salary']

```{{execute windows}}

So we have these five tiny functions which do parts of what we want. How
can we convert them into something that does all this work on this data?

First we'll want to do a pass where we make sure that the fields are
correct (convert ages and salaries to numbers, then convert hourly salaries to
yearly). Then, we'll want to filter out the bad data (empty name or age too
high). The reason for the ordering is that our age checker requires that the
person has an age that is a number, so I want to convert ages to numbers first.

This function will take in a list of `cleaners` (this is the name I picked for
functions that clean up the data by modifying it). Then, it will take a list of
`filters`, or functions that determine if we want to keep them.

```
def clean_data(data, cleaners, filters):
    # first make sure the data is cleaned
    for item in data:
        for cleaner_func in cleaners:
            cleaner_func(item)
    # then keep only the good data
    out = []
    for item in data:
        should_append = True
        for filter in filters:
            # don't add this item if the filter returns False
            if not filter(item):
                should_append = False

        if should_append:
            out.append(item)
    return out
```{{execute windows}}

OK, let's try out this function!

```
clean_data(data,
    cleaners=[convert_age_to_number, convert_salary_to_number, convert_salary_to_yearly],
    filters=[has_empty_name, has_age_over_100])
```{{execute windows}}

This function is easy to understand, and so are all the helpers. And, if you
want to clean the data with a different set of cleaners or filters, it's very
easy to extend this code. You can use it on lots of different datasets
with minimal code copying. I'd call that a success!
