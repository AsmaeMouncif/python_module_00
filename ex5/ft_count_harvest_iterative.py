# *************************************************************************** #
#                                                                             #
#                                                       :::      ::::::::    #
#    ft_count_harvest_iterative.py                    :+:      :+:    :+:    #
#                                                   +:+ +:+         +:+      #
#    By: asmounci <asmounci@student.42.fr>        +#+  +:+       +#+         #
#                                               +#+#+#+#+#+   +#+            #
#    Created: 2026/01/14 13:35:54 by asmounci      #+#    #+#              #
#    Updated: 2026/01/14 17:35:05 by asmounci     ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    i = 1
    while i <= days:
        print("Day", i)
        i = i + 1
    print("Harvest time!")
