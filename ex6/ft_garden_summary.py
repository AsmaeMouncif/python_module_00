# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_summary.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asmounci <asmounci@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/14 14:35:19 by asmounci          #+#    #+#              #
#    Updated: 2026/01/14 18:10:41 by asmounci         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_garden_summary():
    name = input("Enter garden name: ")
    n_plants = int(input("Enter number of plants: "))
    print(f"Garden: {name}")
    print("Plants:", n_plants)
    print("Status: Growing well!")
ft_garden_summary()
