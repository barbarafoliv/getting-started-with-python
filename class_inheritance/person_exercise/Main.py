from Friend import *
from Colleague import *

if __name__=='__main__':
    friend=Friend("Rita", "912 345 678", "Porto", "2015")
    colleague=Colleague("José", "919 876 543", "Doctor", "Hospital")

    friend.print_friend_details()
    colleague.print_colleague_details()
