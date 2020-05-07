import array as arr
from models.Order import *
from models.Date import *

order1 = Order("Birthday1", Date(3, 21, 5, 2020), Date(7, 20, 7, 2020), 2, PriorityCode.Red, Status.Ongoing, 1000)
order2 = Order("Vanilla Cupcakes (25)", Date(1, 11, 5, 2020), Date(7, 20, 7, 2020), 1, PriorityCode.Yellow,
               Status.Ongoing,
               1000)
order3 = Order("Triple Chocolate Cake", Date(7, 30, 5, 2020), Date(7, 20, 7, 2020), 2, PriorityCode.Red, Status.Ongoing,
               20000)
order4 = Order("Strawberry Pie", Date(2, 1, 5, 2020), Date(7, 20, 7, 2020), 2, PriorityCode.Red, Status.Ongoing, 32000)
order5 = Order("Vegan Cake", Date(5, 12, 5, 2020), Date(7, 20, 7, 2020), 1, PriorityCode.Green, Status.Ongoing, 25000)
order6 = Order("Marble cake", Date(6, 2, 5, 2020), Date(6, 17, 5, 2020), 1, PriorityCode.Yellow, Status.Ongoing, 15000)
order7 = Order("Carrot Cake", Date(1, 25, 5, 2020), Date(1, 25, 5, 2020), 2, PriorityCode.Red, Status.Ongoing, 20000)
order8 = Order("Chocolate Croissant (10)", Date(1, 4, 5, 2020), Date(2, 12, 5, 2020), 2, PriorityCode.Red,
               Status.Ongoing, 32000)
order9 = Order("Macaroons (25)", Date(5, 28, 4, 2020), Date(5, 15, 5, 2020), 1, PriorityCode.Green, Status.Ongoing,
               25000)
order10 = Order("Chocolate Chip Cookie", Date(1, 4, 5, 2020), Date(6, 22, 5, 2020), 1, PriorityCode.Yellow,
                Status.Ongoing, 15000)

daisy_orders = {order1.id: order1, order2.id: order2, order3.id: order3,
                order4.id: order4, order5.id: order5, order6.id: order6,
                order7.id: order7, order8.id: order8, order9.id: order9,
                order10.id: order10}

date_collection = {order1.id: order1.due_date, order2.id: order2.due_date,
                   order3.id: order3.due_date, order4.id: order4.due_date,
                   order5.id: order5.due_date, order6.id: order6.due_date,
                   order7.id: order7.due_date, order8.id: order8.due_date,
                   order9.id: order9.due_date, order10.id: order10.due_date}
