from neomodel import StructuredNode, UniqueIdProperty, StringProperty, DateTimeFormatProperty, IntegerProperty, Relationship, RelationshipFrom, RelationshipTo, OneOrMore, One, ZeroOrOne, ZeroOrMore

# Create your models here.
class Person(StructuredNode):
    name = StringProperty(unique_index=True)
    password = StringProperty()
    token = StringProperty(unique_index=True)
    days = RelationshipFrom('Day', 'HAVE', cardinality=OneOrMore)

class Day(StructuredNode):
    date = DateTimeFormatProperty(unique_index=True)
    comment = StringProperty()
    person = RelationshipTo('Person', 'HAVE', cardinality=One)
    pain_evaluations = RelationshipFrom('PainEvaluation', 'DURING', cardinality=ZeroOrMore)
    meals = RelationshipFrom('Meal', 'DURING', cardinality=ZeroOrMore)

    def to_json(self):
        return {
            "id": self.id,
            "date": self.date,
            "comment": self.comment
        }

class Dish(StructuredNode):
    name = StringProperty(unique_index=True)
    category = StringProperty(
        choices={'vegetables': 'Vegetables', 'fruits': 'Fruits', 'meat': 'Meat', 'fish': 'Fish', 'cereals': 'Cereals', 'dairy': 'Dairy', 'sweets': 'Sweets', 'drinks': 'Drinks'}
    )
    meals = Relationship('Meal', 'CONTAINS', cardinality=OneOrMore)

class Meal(StructuredNode):
    type = StringProperty(
        choices={'breakfast': 'Breakfast', 'lunch': 'Lunch', 'snack': 'Snack', 'dinner': 'Dinner', 'others': 'Others'}
    )
    day = RelationshipTo('Day', 'DURING', cardinality=One)
    dishes = Relationship('Dish', 'CONTAINS', cardinality=OneOrMore)

class PainEvaluation(StructuredNode):
    type = StringProperty(
        choices={'morning': 'morning', 'midday': 'Midday', 'evening': 'Evening', 'night': 'Night'}
    )
    value = IntegerProperty()
    day = RelationshipTo('Day', 'DURING', cardinality=One)

    def to_json(self):
        return {
            "type": self.type,
            "value": self.value,
            "day": self.day
        }
