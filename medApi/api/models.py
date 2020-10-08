from neomodel import StructuredNode, StringProperty, DateProperty, IntegerProperty, RelationshipFrom, RelationshipTo, OneOrMore, One

# Create your models here.
class Person(StructuredNode):
    name = StringProperty(unique_index=True)
    password = StringProperty()
    token = StringProperty(unique_index=True)

class Day(StructuredNode):
    date = DateProperty(unique_index=True)
    comment = StringProperty()
    person = RelationshipFrom('Person', 'HAVE', cardinality=One)


class Dish(StructuredNode):
    name = StringProperty(unique_index=True)
    category = StringProperty(
        choices={'vegetables': 'Vegetables', 'fruits': 'Fruits', 'meat': 'Meat', 'fish': 'Fish', 'cereals': 'Cereals', 'dairy': 'Dairy', 'sweets': 'Sweets', 'drinks': 'Drinks'}
    )

class Meal(StructuredNode):
    type = StringProperty(
        choices={'breakfast': 'Breakfast', 'lunch': 'Lunch', 'snack': 'Snack', 'dinner': 'Dinner', 'others': 'Others'}
    )
    day = RelationshipFrom('Day', 'DURING', cardinality=One)
    dishes = RelationshipTo('Dish', 'CONTAINS', cardinality=OneOrMore)

class PainEvaluation(StructuredNode):
    type = StringProperty(
        choices={'morning': 'morning', 'midday': 'Midday', 'evening': 'Evening', 'night': 'Night'}
    )
    value = IntegerProperty()
    day = RelationshipFrom('Day', 'DURING', cardinality=One)
