# TODO
- Make sure root is a dict

- if argument in annotation class is "value" it should treat this directly.
def test(a, b, **value):
>> {propertiues: {a: {},b: {}, test: {}}, additionalProperties: true}
.. test(a, b, test)


- if custom class annotation. raises error: unknown json type