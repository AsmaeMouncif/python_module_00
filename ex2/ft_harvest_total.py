# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asmounci <asmounci@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/14 13:05:14 by asmounci          #+#    #+#              #
#    Updated: 2026/01/14 13:11:45 by asmounci         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: ")) 
    day3 = int(input("Day 3 harvest: "))
    print("Total harvest:", day1 + day2 + day3)

ft_harvest_total()