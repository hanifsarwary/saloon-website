/*global console*/
//calender
//month
//prev
//next
//weeks
//days

//punblic variables
var script = document.createElement("SCRIPT");
    script.src = 'http://code.jquery.com/jquery-latest.min.js';
    script.type = 'text/javascript';

    document.getElementsByTagName("head")[0].appendChild(script);
var calender = document.querySelector(".calender"),//container of calender
    topDiv = document.querySelector('.month'),
    monthDiv = calender.querySelector("h1"),//h1 of monthes
    yearDiv = calender.querySelector('h2'),//h2 for years
    weekDiv = calender.querySelector(".weeks"),//week container
    dayNames = weekDiv.querySelectorAll("li"),//dayes name
    dayItems = calender.querySelector(".days"),//date of day container
    prev = calender.querySelector(".prev"),
    next = calender.querySelector(".next"),

    // date variables
    years = new Date().getFullYear(),
    monthes = new Date(new Date().setFullYear(years)).getMonth(),
    lastDayOfMonth = new Date(new Date(new Date().setMonth(monthes + 1)).setDate(0)).getDate(),
    dayOfFirstDateOfMonth = new Date(new Date(new Date().setMonth(monthes)).setDate(1)).getDay(),

    // array to define name of monthes
    monthNames = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"],
    colors = ['#FFA549', '#ABABAB', '#1DABB8', '#953163', '#E7DF86', '#E01931', '#92F22A', '#FEC606', '#563D28', '#9E58DC', '#48AD01', '#0EBB9F'],
    i,//counter for day before month first day in week
    x,//counter for prev , next
    counter;//counter for day of month  days;

var monthnumber;
var yearnumber;
//display dayes of month in items
function days(x) {
  'use strict';
  dayItems.innerHTML = "";
  monthes = monthes + x;

  /////////////////////////////////////////////////
  //test for last month useful while prev ,max prevent go over array
  if (monthes > 11) {
    years = years + 1;
    monthes = new Date(new Date(new Date().setFullYear(years)).setMonth(0)).getMonth();//ترجع الشهر لاول شهر فى السنه الجديده
  }
  if (monthes < 0) {
    years = years - 1;
    monthes = new Date(new Date(new Date().setFullYear(years)).setMonth(11)).getMonth();//ترجع الشهر لاخر شهر فى السنه اللى فاتت
  }
  //هعرف اخر يوم واول يوم فى الشهر تانى علشان الشهر بيتغير مع next,prev
  lastDayOfMonth = new Date(new Date(new Date(new Date().setFullYear(years)).setMonth(monthes + 1)).setDate(0)).getDate();//اخر يوم فى الشهر
  dayOfFirstDateOfMonth = new Date(new Date(new Date(new Date().setFullYear(years)).setMonth(monthes)).setDate(1)).getDay();//بداية الشهر فى اى يوم من ايام الاسبوع؟
  /////////////////////////////////////////////////
  yearDiv.innerHTML = years;
  monthDiv.innerHTML = monthNames[monthes];
  monthnumber=monthes+1;
  for (i = 0; i <= dayOfFirstDateOfMonth; i = i + 1) {
    if (dayOfFirstDateOfMonth === 6) { break; }
    dayItems.innerHTML += "<li> - </li>";
  }
  for (counter = 1; counter <= lastDayOfMonth; counter = counter + 1) {
    dayItems.innerHTML += '<li id="' + (counter) + '" onClick="reply_click(this.id)">' + (counter) + "</li>";


  }
  topDiv.style.background = colors[monthes];
  dayItems.style.background = colors[monthes];
  //تمييز اليوم الحالى
  if (monthes === new Date().getMonth() && years === new Date().getFullYear()) {
    //فى حالة التاريخ الحالى =الخلفيه خضراء
    dayItems.children[new Date().getDate() + dayOfFirstDateOfMonth].style.background = "#2ecc71";
  }
}
prev.onclick = function () {
  'use strict';
  days(-1);//decrement monthes
};
next.onclick = function () {
  'use strict';
  days(1);//increment monthes
};
days(0);
function reply_click(clicked_id)
{
    var test=clicked_id
    var yearDiv = calender.querySelector('h1'),//h2 for years
    monthDiv = calender.querySelector("h2");
    yearnumber=monthDiv;
 d= {
    'day':test,
    'month':monthnumber,
    'year':years,
    };

     $.ajax({
    url: "/ajax/timing/",
    method: "GET",
    contentType: 'application/json',
    data:d,
    cache: false,

    success: function (data1) {
        window.location.href =data1.url;
//
//var para = document.createElement("p");
//var element = document.getElementById("calender");
//var k;
//$.each(data1, function(index,item){
//                obj=JSON.stringify(item.time);
//                alert(obj);
//                var node = document.createTextNode(obj);
//                para.appendChild(node);
//                element.appendChild(para);
//
//            });
//                        var timings = data1['timings'];
//                        if(timings)
//
//                            {
//                            alert("i am here");
//                                for(var i=0; i<timings.length;i++)
//                                {
//                                    var tmp = (timings[i]);
//                                    alert(tmp);
//                                }
//                            }
//                            else
//                            {
//                                console.log("no result");
//                            }



    },
    error: function () {
        alert("Error")

    }
});


}





//end