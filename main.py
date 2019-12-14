
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PYProject import Ui_MainWindow

# class that creates instance of the GUI
class MyMain(QtWidgets.QMainWindow, Ui_MainWindow):

    # constructor method
    def __init__(self, file):

        # starts gui
        super(MyMain,self).__init__()

        # method that sets up the gui and passes on the data base
        self.setupUi(self,file)

        # setting up the sliders
        self.revenueSlider.setMaximum(self.df["Revenue (Millions)"].max())
        self.revenueSlider.setMinimum(self.df["Revenue (Millions)"].min())
        self.revenueSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.revenueSlider.setTickInterval(self.df["Revenue (Millions)"].mean())

        self.run_time_slider.setMaximum(self.df['Runtime (Minutes)'].max())
        self.run_time_slider.setMinimum(self.df['Runtime (Minutes)'].min())
        self.run_time_slider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.run_time_slider.setTickInterval(self.df['Runtime (Minutes)'].mean())

        # connecting the buttons to the methods
        self.change_layOut_BTN.clicked.connect(self.change_LAYOUT)
        self.max_min_btn.clicked.connect(self.get_Min_Max)
        self.genre_BTN.clicked.connect(self.search_genre)
        self.search_actor_btn.clicked.connect(self.search_actor)
        self.search_director_btn.clicked.connect(self.searchDirector)
        self.srch_rank_btn.clicked.connect(self.srch_top_rank)
        self.revenue_btn.clicked.connect(self.filter_revenue)
        self.runtime_BTN.clicked.connect(self.search_Runtime)
        self.srch_4movies_BTN.clicked.connect(self.srchMovie_Name)

    # method that changes the layout of the graph
    def change_LAYOUT(self):

        # checking the axis layout
        if self.horizontal_radioBtn.isChecked():

            # setting the axis
            x = self.x_axis_comboBox.currentText()
            y = self.y_axis_comboBox.currentText()

            # drawing the graph and information
            self.MplotWidget.canvas.axes.cla()
            self.MplotWidget.canvas.axes.scatter(self.df[x], self.df[y], color="black")
            self.MplotWidget.canvas.axes.set_xlabel(x)
            self.MplotWidget.canvas.axes.set_ylabel(y)
            self.MplotWidget.canvas.draw_idle()

            if y == "Revenue (Millions)":
                actual = "Revenue"
            else:
                actual = y

            self.ma_min_label.setText(self.max_min_combobox.currentText() + " " + actual + ":")
            self.ma_min_label.repaint()

        else:

            # setting the axis
            y = self.x_axis_comboBox.currentText()
            x = self.y_axis_comboBox.currentText()

            # drawing the graph and information
            self.MplotWidget.canvas.axes.cla()
            self.MplotWidget.canvas.axes.scatter(self.df[x], self.df[y], color="black")
            self.MplotWidget.canvas.axes.set_xlabel(x)
            self.MplotWidget.canvas.axes.set_ylabel(y)
            self.MplotWidget.canvas.draw_idle()

            if x == "Revenue (Millions)":
                actual = "Revenue"
            else:
                actual = x

            self.ma_min_label.setText(self.max_min_combobox.currentText() + " " + actual + ":")
            self.ma_min_label.repaint()


    # get min and max method
    def get_Min_Max(self):

        value_type = self.max_min_combobox.currentIndex()

        y = self.y_axis_comboBox.currentText()
        if y == "Revenue (Millions)":
            actual = "Revenue"
        else:
            actual = y

        if value_type == 0 :

            self.ma_min_label.setText(self.max_min_combobox.currentText() + " " + actual + ": "+
                                       str(self.df[self.y_axis_comboBox.currentText()].max()))
            self.ma_min_label.repaint()

        elif value_type == 1:

            self.ma_min_label.setText(self.max_min_combobox.currentText() + " " + actual + ": "+
                                     str(self.df[self.y_axis_comboBox.currentText()].min()))
            self.ma_min_label.repaint()


        else:

            self.ma_min_label.setText(
                self.max_min_combobox.currentText() + " " + actual + ": "+
                str(self.df[self.y_axis_comboBox.currentText()].mean()))
            self.ma_min_label.repaint()

    # search genre method
    def search_genre(self):

        # getting value from combobox
        genre = self.genre_comboBox.currentText()

        if genre != "All":

            # cheking how graph is drawn
            if self.horizontal_radioBtn.isChecked():

                x = self.x_axis_comboBox.currentText()
                y = self.y_axis_comboBox.currentText()

            else:
                y = self.x_axis_comboBox.currentText()
                x = self.y_axis_comboBox.currentText()

            # getting the genres of the movies based on the axis and the choosen value
            movies_xAxis = self.df[x][self.df['Genre'].apply(lambda gen_set: genre in gen_set)]
            movies_yAxis = self.df[y][self.df['Genre'].apply(lambda gen_set: genre in gen_set)]

            # drawing the graph and infomation
            self.MplotWidget.canvas.axes.cla()
            self.MplotWidget.canvas.axes.scatter(self.df[x], self.df[y], color="black")
            self.MplotWidget.canvas.axes.scatter(movies_xAxis, movies_yAxis, color="Red")
            self.MplotWidget.canvas.axes.set_xlabel(x)
            self.MplotWidget.canvas.axes.set_ylabel(y)
            self.MplotWidget.canvas.draw_idle()
            self.movie_info_label.setText(
            genre + ": \nRank\n"+
            self.df[["Title", y]][self.df['Genre'].apply(lambda gen_set: genre in gen_set)].to_string())
            self.movie_info_label.repaint()
            self.director_searchbox.clear()
            self.actor_searchbox.clear()
            self.revenu_Label.setText("Revenue: ")
            self.runtime_label.setText("Runtime:")
            self.revenu_Label.repaint()
            self.runtime_label.repaint()

        else:
            x = self.x_axis_comboBox.currentText()
            y = self.y_axis_comboBox.currentText()
            self.MplotWidget.canvas.axes.cla()
            self.MplotWidget.canvas.axes.scatter(self.df[x], self.df[y], color="black")
            self.MplotWidget.canvas.axes.set_xlabel(x)
            self.MplotWidget.canvas.axes.set_ylabel(y)
            self.MplotWidget.canvas.draw_idle()
            self.movie_info_label.setText( "All Movies: \nRank               "
                                                                   "                             Ttitle\n" +
                                                     self.df["Title"].to_string())
            self.movie_info_label.repaint()
            self.director_searchbox.clear()
            self.actor_searchbox.clear()
            self.revenu_Label.setText("Revenue: ")
            self.runtime_label.setText("Runtime:")
            self.revenu_Label.repaint()
            self.runtime_label.repaint()


    # search actor method
    def search_actor(self):

        # getting actor name
        actor = self.actor_searchbox.text()

        # cheking if there is infomation in the text box
        if len(actor) != 0:

            # getting the tittles of the movies the actor has played in
            titles = self.df["Title"][self.df["Actors"].apply(lambda act_list: actor in act_list)]

            # if that actor exist in any movies go here
            if titles.size > 0:

                # checking the layout of the graph
                if self.horizontal_radioBtn.isChecked():

                    x = self.x_axis_comboBox.currentText()
                    y = self.y_axis_comboBox.currentText()

                else:
                    y = self.x_axis_comboBox.currentText()
                    x = self.y_axis_comboBox.currentText()

                # getting all the movies based of the axis that the actor has played in
                moviesX = self.df[x][self.df["Actors"].apply(lambda act_list: actor in act_list)]
                moviesY = self.df[y][self.df["Actors"].apply(lambda act_list: actor in act_list)]

                # drawing the graph and infomation
                self.MplotWidget.canvas.axes.cla()
                self.MplotWidget.canvas.axes.scatter(self.df[x], self.df[y], color="black")
                self.MplotWidget.canvas.axes.scatter(moviesX, moviesY, color="orange")
                self.MplotWidget.canvas.axes.set_xlabel(x)
                self.MplotWidget.canvas.axes.set_ylabel(y)
                self.MplotWidget.canvas.draw_idle()
                self.movie_info_label.setText(
                "Actor: " + actor + "\n\nTotal Movies: " + str(titles.size) + "\n\nTitles: \n\nRank\n" + titles.to_string()

                )
                self.movie_info_label.repaint()
                self.director_searchbox.clear()
                self.revenu_Label.setText("Revenue: ")
                self.runtime_label.setText("Runtime:")
                self.revenu_Label.repaint()
                self.runtime_label.repaint()

            # if no actor found go here
            else:
                self.movie_info_label.setText("No Actors with that name in our database :(")
                self.movie_info_label.repaint()
                self.director_searchbox.clear()
                self.revenu_Label.setText("Revenue: ")
                self.runtime_label.setText("Runtime:")
                self.revenu_Label.repaint()
                self.runtime_label.repaint()

        # if the box was empty go here
        else:
            self.movie_info_label.setText("Please enter an actor to search of actor!")
            self.movie_info_label.repaint()
            self.director_searchbox.clear()
            self.revenu_Label.setText("Revenue: ")
            self.runtime_label.setText("Runtime:")
            self.revenu_Label.repaint()
            self.runtime_label.repaint()

    # search for director method
    def searchDirector(self):

        # getting value
        director = self.director_searchbox.text()

        # checking if there was anything in the value
        if len(director) != 0:

            # getting the titles based of the director
            titles = self.df["Title"][self.df["Director"] == director]

            # if there are any titles the director has made go here
            if titles.size > 0:

                # checking lay out of graph
                if self.horizontal_radioBtn.isChecked():

                    x = self.x_axis_comboBox.currentText()
                    y = self.y_axis_comboBox.currentText()

                else:
                    y = self.x_axis_comboBox.currentText()
                    x = self.y_axis_comboBox.currentText()

                # getting movies based on the axis
                moviesX = self.df[x][self.df["Director"] == director]
                moviesY = self.df[y][self.df["Director"] == director]

                # drawing the graph and information
                self.MplotWidget.canvas.axes.cla()
                self.MplotWidget.canvas.axes.scatter(self.df[x], self.df[y], color="black")
                self.MplotWidget.canvas.axes.scatter(moviesX, moviesY, color="magenta")
                self.MplotWidget.canvas.axes.set_xlabel(x)
                self.MplotWidget.canvas.axes.set_ylabel(y)
                self.MplotWidget.canvas.draw_idle()
                self.movie_info_label.setText(
                    "Director: " + director + "\n\nTotal Movies: " + str(
                        titles.size) + "\n\nTitles: \n\nRank\n" + titles.to_string()
                )
                self.movie_info_label.repaint()
                self.actor_searchbox.clear()
                self.revenu_Label.setText("Revenue: ")
                self.runtime_label.setText("Runtime:")
                self.revenu_Label.repaint()
                self.runtime_label.repaint()

            # if there are nio director go here
            else:

                self.movie_info_label.setText("No Director with that name :(")
                self.movie_info_label.repaint()
                self.actor_searchbox.clear()
                self.revenu_Label.setText("Revenue: ")
                self.runtime_label.setText("Runtime:")
                self.revenu_Label.repaint()
                self.runtime_label.repaint()
        # if there is no ifmoration go here
        else:
            self.movie_info_label.setText("Please enter a Director to search of Director!")
            self.movie_info_label.repaint()
            self.actor_searchbox.clear()
            self.revenu_Label.setText("Revenue: ")
            self.runtime_label.setText("Runtime:")
            self.revenu_Label.repaint()
            self.runtime_label.repaint()

    # searching by top rank method
    def srch_top_rank(self):

        # checking if there information in txt box
        if len(self.rank_searchbox.text()) != 0:

            # try and except to make sure user puts numeric value
            try:
                # getting rank from box and setting it as int
                user_rank = int(self.rank_searchbox.text())

                # getting any tittle thats that rank or less
                titles = self.df["Title"][self.df["Rank"] <= user_rank]

                # if titles of that rank or less exist go here
                if titles.size <= self.df.size:

                    # checking layout
                    if self.horizontal_radioBtn.isChecked():
                        x = self.x_axis_comboBox.currentText()
                        y = self.y_axis_comboBox.currentText()
                    else:
                        y = self.x_axis_comboBox.currentText()
                        x = self.y_axis_comboBox.currentText()

                    # getting movie info and paining graph
                    moviesX = self.df[x][self.df["Rank"] <= user_rank]
                    moviesY = self.df[y][self.df["Rank"] <= user_rank]

                    self.MplotWidget.canvas.axes.cla()
                    self.MplotWidget.canvas.axes.scatter(self.df[x], self.df[y], color="black")
                    self.MplotWidget.canvas.axes.scatter(moviesX, moviesY, color="lawngreen")
                    self.MplotWidget.canvas.axes.set_xlabel(x)
                    self.MplotWidget.canvas.axes.set_ylabel(y)
                    self.MplotWidget.canvas.draw_idle()

                    self.movie_info_label.setText(
                        "Top " + str(user_rank) + " Movies: \n\n" + titles.to_string()
                    )
                    self.movie_info_label.repaint()

                    self.director_searchbox.clear()
                    self.actor_searchbox.clear()
                    self.revenu_Label.setText("Revenue: ")
                    self.runtime_label.setText("Runtime:")
                    self.revenu_Label.repaint()
                    self.runtime_label.repaint()

                # if no ranks exist display this message
                else:
                    self.movie_info_label.setText(
                        "Please enter a rank of " + str(self.df.size) + " or lower!"
                    )
                    self.movie_info_label.repaint()
                    self.director_searchbox.clear()
                    self.actor_searchbox.clear()
                    self.revenu_Label.setText("Revenue: ")
                    self.runtime_label.setText("Runtime:")
                    self.revenu_Label.repaint()
                    self.runtime_label.repaint()

            # if the user does not put a number display error message
            except ValueError:
                self.movie_info_label.setText(
                    "To search for rank please enter a NUMBER!"
                )
                self.movie_info_label.repaint()

                self.director_searchbox.clear()
                self.actor_searchbox.clear()
                self.revenu_Label.setText("Revenue: ")
                self.runtime_label.setText("Runtime:")
                self.revenu_Label.repaint()
                self.runtime_label.repaint()
                
        # blank box error message
        else:
            self.movie_info_label.setText(
                "Enter a number to search for rank"
            )
            self.movie_info_label.repaint()

            self.director_searchbox.clear()
            self.actor_searchbox.clear()
            self.revenu_Label.setText("Revenue: ")
            self.runtime_label.setText("Runtime:")
            self.revenu_Label.repaint()
            self.runtime_label.repaint()

    # searching by revenue slider method
    def filter_revenue(self):

        # getting value in slider
        revenue = self.revenueSlider.value()

        # setting label with value in slider
        self.revenu_Label.setText("Revenue: " + str(revenue))
        self.revenu_Label.repaint()

        # checking layout
        if self.horizontal_radioBtn.isChecked():

            x = self.x_axis_comboBox.currentText()
            y = self.y_axis_comboBox.currentText()

        else:
            y = self.x_axis_comboBox.currentText()
            x = self.y_axis_comboBox.currentText()

        # getting information and paining graph

        moviesX = self.df[x][self.df["Revenue (Millions)"] >= revenue]
        moviesY = self.df[y][self.df["Revenue (Millions)"] >= revenue]

        self.MplotWidget.canvas.axes.cla()
        self.MplotWidget.canvas.axes.scatter(self.df[x], self.df[y], color="black")
        self.MplotWidget.canvas.axes.scatter(moviesX, moviesY, color="gold")
        self.MplotWidget.canvas.axes.set_xlabel(x)
        self.MplotWidget.canvas.axes.set_ylabel(y)
        self.MplotWidget.canvas.draw_idle()

        self.movie_info_label.setText(
            "Movie Revenue minimum of: " + str(revenue) + " Million\n Movies: \n\n" +
            self.df["Title"][self.df["Revenue (Millions)"] >= revenue].to_string()
        )
        self.movie_info_label.repaint()

        self.director_searchbox.clear()
        self.actor_searchbox.clear()
        self.runtime_label.setText("Runtime:")
        self.runtime_label.repaint()

    # searching by runtime slider method
    def search_Runtime(self):

        # getting value in slider
        runtime = self.run_time_slider.value()

        # setting label with the value selected
        self.runtime_label.setText("Run Time: " + str(runtime))
        self.runtime_label.repaint()

        # checking the layout
        if self.horizontal_radioBtn.isChecked():

            x = self.x_axis_comboBox.currentText()
            y = self.y_axis_comboBox.currentText()

        else:
            y = self.x_axis_comboBox.currentText()
            x = self.y_axis_comboBox.currentText()


        # getting info and paiting graph
        moviesX = self.df[x][self.df["Runtime (Minutes)"] >= runtime]
        moviesY = self.df[y][self.df["Runtime (Minutes)"] >= runtime]

        self.MplotWidget.canvas.axes.cla()
        self.MplotWidget.canvas.axes.scatter(self.df[x], self.df[y], color="black")
        self.MplotWidget.canvas.axes.scatter(moviesX, moviesY, color="blue")
        self.MplotWidget.canvas.axes.set_xlabel(x)
        self.MplotWidget.canvas.axes.set_ylabel(y)
        self.MplotWidget.canvas.draw_idle()

        self.movie_info_label.setText("Movies Runtime minimum: " + str(runtime) + " Minutes\n "
                                                                             "Movies\n\n" +
                                      self.df["Title"][self.df["Runtime (Minutes)"] >= runtime].to_string()
                                      )
        self.movie_info_label.repaint()
        self.director_searchbox.clear()
        self.actor_searchbox.clear()
        self.revenu_Label.setText("Revenue: ")
        self.revenu_Label.repaint()

    # searching by movie name
    def srchMovie_Name(self):

        # getting value in label
        movieName = self.srch_4movies_searchBox.text()

        # if the search bos is not empty go here
        if len(movieName) != 0:

            # checking lay out
            if self.horizontal_radioBtn.isChecked():
                x = self.x_axis_comboBox.currentText()
                y = self.y_axis_comboBox.currentText()
            else:
                y = self.x_axis_comboBox.currentText()
                x = self.y_axis_comboBox.currentText()


            # checking if actor exist in database
            movie = self.df.loc[self.df["Title"] == movieName]

            # if so go here
            if len(movie) > 0:

                # getting information and painting graph
                moviesX = self.df[x][self.df["Title"] == movieName]
                moviesY = self.df[y][self.df["Title"] == movieName]

                self.MplotWidget.canvas.axes.cla()
                self.MplotWidget.canvas.axes.scatter(self.df[x], self.df[y], color="black")
                self.MplotWidget.canvas.axes.scatter(moviesX, moviesY, color="crimson")
                self.MplotWidget.canvas.axes.set_xlabel(x)
                self.MplotWidget.canvas.axes.set_ylabel(y)
                self.MplotWidget.canvas.draw_idle()

                self.movie_info_label.setText(movieName + " Info: \n" + movie.to_string())
                self.movie_info_label.repaint()

                self.director_searchbox.clear()
                self.revenu_Label.setText("Revenue: ")
                self.runtime_label.setText("Runtime:")
                self.revenu_Label.repaint()
                self.runtime_label.repaint()

            # else display no actors in database
            else:
                self.movie_info_label.setText("There are no movies witht hat tittle :(")
                self.movie_info_label.repaint()

                self.director_searchbox.clear()
                self.revenu_Label.setText("Revenue: ")
                self.runtime_label.setText("Runtime:")
                self.revenu_Label.repaint()
                self.runtime_label.repaint()

        else:
            # else show error message of information needed to be in search box
            self.movie_info_label.setText("Please enter a MOVIE to search by movie tittle")
            self.movie_info_label.repaint()

            self.director_searchbox.clear()
            self.revenu_Label.setText("Revenue: ")
            self.runtime_label.setText("Runtime:")
            self.revenu_Label.repaint()
            self.runtime_label.repaint()

# starting the gui
if __name__ == "__main__":

    file = "/Users/ervinlara/PycharmProjects/FinalProject/IMDB-Movie-Data.csv"

    app = QtWidgets.QApplication(sys.argv)
    window = MyMain(file)
    window.show()
    sys.exit(app.exec_())

