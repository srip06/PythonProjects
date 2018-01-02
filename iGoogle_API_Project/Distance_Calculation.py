#to link with internet urls we need to import urllib.request
import urllib


class Tour(object):
    
    """this is a constructor when an object is created, places will be stored in the self.places, the varaibles which are with
    self can be accessable through out the class"""
    def __init__(self,*places):
        self.places = []
        for i in places:
            self.places.append(i)


    """in this function we wiil caculate the total distance from one place to the destination with the given mode"""
    def distance(self,*mode):
        if mode == ():
            mode1 = "driving"
        else:
            mode1 = mode[0]
        #print "mode ",mode1
        total_dis = []
        """ this will iterates though all the places until the destination is reached"""
        for i in range(len(self.places)-1):
            """if there is no origin or destination it will raise a value error"""
            if self.places[i] == "":
                raise ValueError('No origin')
            if self.places[i+1] == "":
                raise ValueError('No destination')
            #here it will split state name and short cut
            origin = self.places[i].split(",")
            destination = self.places[i+1].split(",")
            #it creates string for url
            u = "http://maps.googleapis.com/maps/api/distancematrix/json?origins="+origin[0]+"+"+origin[1]+"&destinations="+destination[0]+"+"+destination[1]+"&mode="+mode1+"&sensor=false"
            web_object = urllib.urlopen(u)
            str_obj = str(web_object.read())
            web_object.close()
            #from here the string will be parsed to get distance value
            str_obj = str_obj.replace('\n',' ').replace('\t',' ')
            s = ""
            for j in range(len(str_obj)):
                if str_obj[j] != ' ':
                    s += str_obj[j]
            #print s
            word = "distance"
            dis_str = ""
            if s.find(word) < 0:
                raise ValueError('distance is not found')
            for c in s[s.find(word)+len(word)+2:]:
                dis_str += c
                if c == '}':
                    break
            dis_val = ""
            for c in dis_str[dis_str.find("value")+len("value")+2:]:
                if c == '}':
                    break
                else:
                    dis_val += c
            #print "distance ",dis_val
            """append each distance between all places"""
            total_dis.append(int(dis_val))
        sum = 0
        """calculate all the distances """
        for j in total_dis:
            sum += j
        #print "total distance ",sum
        return sum        


    """it returns the string representation of an object instance"""
    def __str__(self):
        s = ""
        for i in range(len(self.places)):
            s += str(self.places[i])+";"
        return s


    """this is the same representation as like __str__()"""
    def __repr__(self):
        return self.__str__()


    """in this on tour's places will be contacted with the other tours placess"""
    def __add__(self,ob):
        """in this an empty list is created and will append all the tour places to it"""
        newtour_places = []
        for i in self.places:
            newtour_places.append(i)
        for i in ob.places:
            newtour_places.append(i)
        """after creating the tour list, it creates the new object"""
        newob = Tour(*newtour_places)
        return newob


    """ in this the tour places will be cycled recursively"""
    def __mul__(self,k):
        """if the given k's value is not integer type it will raise type error, if it is negative integer it will raise value error"""
        if type(k) != int:
            raise TypeError('It is not integer')
        if k <= 0:
            raise ValueError('It is negative integer, should multiply with postive integer')
        """in thsi also , it creates a new list to append all the places of the tour manny times given thought the argumnet"""
        """it will append the places in the reverse order for every second tour to create a cycle"""
        newtour_places = []
        #print "self.places ",self.places
        for j in range(k):
            if j%2 == 0:
                for i in self.places:
                    newtour_places.append(i)
            else:
                for i in list(reversed(self.places)):
                    newtour_places.append(i)
        #print newtour_places
        return Tour(*newtour_places)


    """this is same as __mul__() whicnh is usefull for the expressions like 'n*ob' where n is integer."""
    def __rmul__(self,k):
        """so this returns the mul function with the k as integer"""
        return self.__mul__(k)


    """in this funtion tours will be compared with coresponding to distance only in driving mode"""
    def __gt__(self,tourob):
        if self.distance() > tourob.distance():
            """return true when left side tour is greater than the right tour"""
            return True
        else:
            return False


    """this is sam like __gt__()"""
    def __lt__(self,tourob):
        if self.distance() < tourob.distance():
            return True
        else:
            return False


    """in this the cycle of tours will be compared"""
    def __eq__(self,ob):
        """if they are equal it will return ture otherwise false"""
        if self.__str__() == ob.__str__():
            return True
        else:
            return False
            
        
def main():

    """created three objects """
    t1 = Tour("New York,NY","Lansing,MI","Sacramento,CA")
    t2 = Tour("Oakland,CA")
    t3 = Tour("Sacramento,CA","Oakland,CA")

    """here we will test all the tours distances and tour places"""
    print("t1:{}\nt2:{}\nt3:{}".format(t1,t2,t3))
    print "t3:driving distance-",t3.distance()
    """tested with all the modes for a tour"""
    print("t1 distances:driving-{}km;biking-{}km;walking-{}km".format(round(t1.distance()/1000),round(t1.distance("biking")/1000),round(t1.distance("walking")/1000)))
    print "Using driving distances from here on."

    """here we will test add function """
    t4 = t1 + t2
    print "t4:",t4
    print"t4 driving distance:",round(t4.distance()/1000),"km"
    print "t4 == t1 + t2:",t4 == t1 + t2
    """testing multiplication"""
    t5 = t1*3
    print "t5:",t5.__str__()
    print "t5-driving:",round(t5.distance()/1000),"km"

    """ testing between tours whether they are greater or lesser or equal"""
    print "t1 > t2:",t1 > t2
    print "t4 < t1:",t4 < t1
    print "t4 == t1+t2: ",t4 == t1+t2
    t6 = t1*1
    print "t6 == t1:",t6 == t1


if __name__ == '__main__':
    main()

