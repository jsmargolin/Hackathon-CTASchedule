# CTASchedule
A back-end program meant to be utilized by the CTA in order to optimize train schedules based on user data.
It was created during a 24 hour high school Hackathon, so there are some bad coding practices, and some
evidence of workarounds. The idea behind this is to analyze the user data that the CTA already has in order to
minimize the total wait time. In order to make it easily implementable, I used completely randomized pseudo-data
for users (location, time) and maps (locations of routes). Before optimization, I spread the train times out 
evenly and used thisas the benchmark for comparison. After optimization, it appeared to reduce total wait time 
by about 30%. Since this was created in a short time period, I simplified some aspects and didn't focus on the UI.
This repository is kept exactly the same as at the end of the hackathon so any mistakes are still here. 

Intentional Simplifications:
<ul>
  <li>Classified a line that can be traveled in two directions (ie: North or South) as two different lines</li>
  <li>Created map with x and y coordinates, in real life I would change to latitude and longitude.</li>
  <li>Only randomly created lines that go top-left to bottom-right and handled those cases because it wouldn't change anything.</li>
  <li>Alloted next to no time to UI since real world implementation is a back-end add on, so there wouldn't even be a UI.</li>
  <li>Measured time on a scale from 0 to 2400 hundreths of an hour from midnight.</li>
  <li>Only used one day of data because it is randomly generated pseudodata that wouldn't have real patterns across days</li>
  <li>Assumed each line has a certain amount of trains they can send per day.</li>
  <li>I worked on this by myself, so I added this onto github after the fact and could easily have forgotten things</li>
</ul>

Mistakes/Future Expansion:
<ul>
    <li>When I created the offset for calculating wait time I forgot to multiply the distance by a constant speed to get the time offset
    and accidentally offset the time by a distance.</li>
    <li>Total wait time probably isn't the best metric since waiting at different times of the day aren't always as important.</li>
    <li>Clean up/comment the code.</li>
    <li>Potentially more, any feedback is appreciated.</li>
</ul>
