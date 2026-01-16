# *************************************************************************** #
#                                                                             #
#                                                       :::      ::::::::    #
#    ft_count_harvest_recursive.py                    :+:      :+:    :+:    #
#                                                   +:+ +:+         +:+      #
#    By: asmounci <asmounci@student.42.fr>        +#+  +:+       +#+         #
#                                               +#+#+#+#+#+   +#+            #
#    Created: 2026/01/14 17:23:56 by asmounci      #+#    #+#              #
#    Updated: 2026/01/14 17:35:02 by asmounci     ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    
    def ft_recursive(n):
        if n > days:
            print("Harvest time!")
        else:
            print("Day", n)
            ft_recursive(n + 1)
    
    ft_recursive(1)
ft_count_harvest_recursive()