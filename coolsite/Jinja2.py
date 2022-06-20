from jinja2 import Template

cars = [
    {'model': 'Mersedes', 'price': 2900},
    {'model': 'BMW', 'price': 3200},
    {'model': 'Audi', 'price': 3500}
]
tpl = "Sum of all auto is {{car | sum(attribute = 'price')}}"
tm = Template(tpl)
msg = tm.render(car=cars)

print(msg)
