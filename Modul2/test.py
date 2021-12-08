class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None
        self.previous = None
          
class Playlist:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.current = None
        
    def isEmpty(self):
        return self.head is None and self.tail is None

    def addSong(self, title, artist):
        if self.isEmpty():
            newSong = Song(title, artist)
            self.head = newSong
            self.tail = newSong
            self.current = newSong
        else:
            newSong = Song(title, artist)
            newSong.previous = self.tail
            self.tail.next = newSong
            self.tail = newSong

    def playSong(self):
        self.current = self.head
        if self.isEmpty():
            return "playlist is empty!.\nPlease add Song to the playlist first!"
        result = self.current.title, self.current.artist
        finale = ' by '.join(result)
        return finale
    
    def playNextSong(self):
        if self.isEmpty():
            return "playlist is empty!."
        if self.current.next is None:
            # means we are in the end of list
            # back to head again
            self.current = self.head
            return "End Of Playlist!"
        
        self.current = self.current.next
        result = self.current.title, self.current.artist
        finale = ' by '.join(result)
        return finale

    def playPreviousSong(self):
        if self.isEmpty():
            return "playlist is empty!."
        if self.current.previous is None:
            # means we are in the beginning of list
            # back to tail again
            return "Already in first Song!"

        self.current = self.current.previous
        result = self.current.title, self.current.artist
        finale = ' by '.join(result)
        return finale

    def printPlaylists(self):
        if self.isEmpty():
            print("playlist is empty.\nAdd Song First!")

        song = self.head
        index = 1
        
        while song is not None:
            print(f"{index}: {song.title} - {song.artist}")
            song = song.next
            index +=1
            
    def removeSong(self,title, artist):
        if self.isEmpty():
            return "playlist is empty"
        current = self.head
        deleted = False
        
        # if current is None:
        #     deleted = False
        if current.title == title and current.artist == artist:
            self.head = current.next
            self.head.previous = None
            deleted = True
        elif self.tail.title == title and self.tail.artist == artist:
            self.tail = self.tail.previous
            self.tail.next = None
            deleted = True
        else:
            while current:
                if current.title == title and current.artist == artist:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                current = current.next
        if deleted:
            return "Succesfull Delete!"

          
if __name__ == '__main__':
    playlist = Playlist()
    print(''''
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&(///////////////////#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@///////////////////////////////@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@&///////////////////////////////////////@&@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@/////////////////////////////////////////////@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@/////////////////////////////////////////////////@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@/////////////////////////////////////////////////////@@@@@@@@@@@@@
@@@@@@@@@@@@&//////////////////////((//*////////////////////////////@@@@@@@@@@@@
@@@@@@@@@@@////////*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@////////////////%@@@@@@@@@@
@@@@@@@@@@(////////@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@//////////&@@@@@@@@@
@@@@@@@@@@//////////@@@/////////////////////////*&@&@@@@@@@@@@@////////@@@@@@@@@
@@@@@@@@@///////////////////////////////////////////////#@@@@@@/////////@@@@@@@@
@@@@@@@@@//////////////&@@@@@@@@@@@@@@@@@@@@@@@#////////////////////////@@@@@@@@
@@@@@@@@@////////////&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@(/////////////////@@@@@@@@
@@@@@@@@@//////////////%///////////////////////@@@@@@@@@@@&/////////////@@@@@@@@
@@@@@@@@@////////////////////////////////////////////&@@@@@/////////////@@@@@@@@
@@@@@@@@@@//////////////%@@@@@@@@@@@@@@@@@@@@%/////////////////////////@@@@@@@@@
@@@@@@@@@@#///////////@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@//////////////////&@@@@@@@@@
@@@@@@@@@@&#////////////////////////////////////@@@@@@@//////////////&@@@@@@@@@@
@@@@@@@@@@@@@///////////////////////////////////////////////////////@@@@@@@@@@@@
@@@@@@@@@@@@@@/////////////////////////////////////////////////////@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@/////////////////////////////////////////////////@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@////////////////////////////////////////////#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@///////////////////////////////////////@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@//////////////////////////////*@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@///////////////////@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    ''')
    while True:
        print('''\n==============Spotify==============
        1. Create a new playlist
        2. Play the song
        3. Play next song
        4. Play previous song
        5. Open Playlist
        6. Delete Song
        7. Exit playlist
        ''')

        menus = int(input('Choice Menu: '))
        
        match menus:
            case 1:
                numberOfSongs = int(input('How Many songs do you want to add to the playlist: '))
                for i in range(numberOfSongs):
                    userInput = input(f'Add Song number {i+1} (Title, Artist): ')
                    splittedInput = userInput.split(",")
                    playlist.addSong(splittedInput[0], splittedInput[1])
                    print("Succesfull Adding Song to Playlist")
            case 2:
                print(f"Now Playing : {playlist.playSong()}")
            case 3:
                print(f"Now Playing : {playlist.playNextSong()}")
            case 4:
                print(f"Now Playing : {playlist.playPreviousSong()}")
            case 5:
                print("==============Spotify Playlist =================")
                playlist.printPlaylists()
            case 6:
                userInput = input("Masukkan lagu yang ingin di delete (title,artist): ")
                splittedInput = userInput.split(",")
                playlist.removeSong(splittedInput[0],splittedInput[1])
            case 7:
                print("See yaa!")
                break
            case _:
                print("Invalid Menu!")