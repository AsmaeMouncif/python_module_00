# *************************************************************************** #
#                                                                             #
#                                                       :::      ::::::::    #
#    ft_plant_age.py                                 :+:      :+:    :+:    #
#                                                   +:+ +:+         +:+      #
#    By: asmounci <asmounci@student.42.fr>        +#+  +:+       +#+         #
#                                               +#+#+#+#+#+   +#+            #
#    Created: 2026/01/14 13:14:42 by asmounci      #+#    #+#              #
#    Updated: 2026/01/14 13:25:21 by asmounci     ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_plant_age():
    plant_age = int(input("Enter plant age in days: "))
    if plant_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
