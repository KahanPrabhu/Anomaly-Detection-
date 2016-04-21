#clear workspace
rm(list=ls(all=T))

#source('installPackages.R') #Install all necessary packages

#load required packages
library(lattice)
require(rworldmap) #for mapGriddedData
require(jpeg)

#read matfile
parent<-"C:/Users/jcgsv/Documents/GitHub/Anomaly-Detection-/topcsvmatrices/"
parent2<-"C:/Users/jcgsv/Documents/GitHub/Anomaly-Detection-/topcsvplot/"
#plots<- "~/ORNL/MonsterRidges/MonsterRidges/"

#create jpeg file
for( i in 0:34){
        for(j in 0:364){
                jpegfile<-paste(parent2,"p",i,"-",j,".jpg",sep="")
                jpeg(jpegfile,width=1024,height=1024)
                
                filename<-paste(parent,i,"-",j,".csv",sep="")
                print(filename)
                data<-read.csv(filename,header = F)
                #Extract just the surface temperatures from the data
                #this is a 3-D numeric vector of dimensions 366 x 73 x 144
                #a 73x144 lat-long grid for each day of the year of 1948
                
                
                #Extract daily lat-long grid for localized spatial analysis
                #so this is a 73 x 144 lat-long grid
                day<-data[,,]
                #THIS MAY BE WRONG. swap left and right halves of data because longitudes vary
                #from 0 to 357.5 (360) as opposed to -180 to +180
                #day<-day[,c(73:144,1:72)]
                
                #transpose the matrix and reverse row ordering (column ordering)
                #in order to provide appropriate input to plotting function
                day<-t(day)
                day<-day[,ncol(day):1]
                
                #make the plot using mapGriddedData function
                mapGriddedData(day,borderCol="black",numCats=20, colourPalette=c('white','red'),catMethod = "categorical")
                
                #write the title as the day and year
                title(paste('Day ',i,' Year ',j,sep = ""))
                dev.off()
        }
}