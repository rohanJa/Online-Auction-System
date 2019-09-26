function h1(){
var y= fruits[0][0]; var mo = fruits[0][1]; var d= fruits[0][2]; var h = fruits[0][3];var m= fruits[0][4]; var s= fruits[0][5];
//document.getElementById('de').innerHTML = '2nditem';
var t = new Date(y,mo,d,h,m,s).getTime();
var x = setInterval(function() {

    // Get todays date and time
    var now = new Date().getTime();
    //var now = new Date(y1,mo1,d1,h1,m1,s1).getTime();
    // Find the distance between now an the count down date
    var distance = t - now;
    
    // Time calculations for days, hours, minutes and seconds
    //var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    // Output the result in an element with id="demo"
    document.getElementById(pid[0]).innerHTML =  hours + "h "
    + minutes + "m " + seconds + "s ";
    
    // If the count down is over, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById(pid[0]).innerHTML = "EXPIRED";
    }
}, 1000);
}
function h2(){
var y1= fruits[1][0]; var mo1 = fruits[1][1]; var d1= fruits[1][2]; var h1 = fruits[1][3];var m1= fruits[1][4]; var s1= fruits[1][5];
//document.getElementById('de').innerHTML = '2nditem';
var t = new Date(y1,mo1,d1,h1,m1,s1).getTime();
var x = setInterval(function() {

    // Get todays date and time
    var now = new Date().getTime();
    //var now = new Date(y1,mo1,d1,h1,m1,s1).getTime();
    // Find the distance between now an the count down date
    var distance = t - now;
    
    // Time calculations for days, hours, minutes and seconds
    //var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    // Output the result in an element with id="demo"
    document.getElementById(pid[1]).innerHTML =  hours + "h "
    + minutes + "m " + seconds + "s ";
    
    // If the count down is over, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById(pid[1]).innerHTML = "EXPIRED";
    }
}, 1000);}
function h3(){
var y2= fruits[2][0]; var mo2 = fruits[2][1]; var d2= fruits[2][2]; var h2 = fruits[2][3];var m2= fruits[2][4]; var s2= fruits[2][5];
//document.getElementById('de').innerHTML = '2nditem';
var t = new Date(y2,mo2,d2,h2,m2,s2).getTime();
var x = setInterval(function() {

    // Get todays date and time
    var now = new Date().getTime();
    //var now = new Date(y1,mo1,d1,h1,m1,s1).getTime();
    // Find the distance between now an the count down date
    var distance = t - now;
    
    // Time calculations for days, hours, minutes and seconds
    //var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    // Output the result in an element with id="demo"
    document.getElementById(pid[2]).innerHTML =  hours + "h "
    + minutes + "m " + seconds + "s ";
    
    // If the count down is over, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById(pid[2]).innerHTML = "EXPIRED";
    }
}, 1000);}
function h4(){
var y3= fruits[3][0]; var mo3 = fruits[3][1]; var d3= fruits[3][2]; var h3 = fruits[3][3];var m3= fruits[3][4]; var s3= fruits[3][5];
//document.getElementById('de').innerHTML = '2nditem';
var t = new Date(y3,mo3,d3,h3,m3,s3).getTime();
var x = setInterval(function() {

    // Get todays date and time
    var now = new Date().getTime();
    //var now = new Date(y1,mo1,d1,h1,m1,s1).getTime();
    // Find the distance between now an the count down date
    var distance = t - now;
    
    // Time calculations for days, hours, minutes and seconds
    //var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    // Output the result in an element with id="demo"
    document.getElementById(pid[3]).innerHTML =  hours + "h "
    + minutes + "m " + seconds + "s ";
    
    // If the count down is over, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById(pid[3]).innerHTML = "EXPIRED";
    }
}, 1000);}
function h5(){
var y4= fruits[4][0]; var mo4 = fruits[4][1]; var d4= fruits[4][2]; var h4 = fruits[4][3];var m4= fruits[4][4]; var s4= fruits[4][5];
//document.getElementById('de').innerHTML = '2nditem';
var t = new Date(y4,mo4,d4,h4,m4,s4).getTime();
var x = setInterval(function() {

    // Get todays date and time
    var now = new Date().getTime();
    //var now = new Date(y1,mo1,d1,h1,m1,s1).getTime();
    // Find the distance between now an the count down date
    var distance = t - now;
    
    // Time calculations for days, hours, minutes and seconds
    //var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    // Output the result in an element with id="demo"
    document.getElementById(pid[4]).innerHTML =  hours + "h "
    + minutes + "m " + seconds + "s ";
    
    // If the count down is over, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById(pid[4]).innerHTML = "EXPIRED";
    }
}, 1000);}
function li1(){
var yl= veg[0][0]; var mol = veg[0][1]; var dl= veg[0][2]; var hl = veg[0][3];var ml= veg[0][4]; var sl= veg[0][5];
//document.getElementById('de').innerHTML = '2nditem';
var t = new Date(yl,mol,dl,hl,ml,sl).getTime();
var x = setInterval(function() {

    // Get todays date and time
    var now = new Date().getTime();
    //var now = new Date(y1,mo1,d1,h1,m1,s1).getTime();
    // Find the distance between now an the count down date
    var distance = t - now;
    
    // Time calculations for days, hours, minutes and seconds
    //var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    // Output the result in an element with id="demo"
    document.getElementById(lid[0]).innerHTML =  hours + "h "
    + minutes + "m " + seconds + "s ";
    
    // If the count down is over, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById(lid[0]).innerHTML = "EXPIRED";
    }
}, 1000);}
function li2(){
var yl2= veg[1][0]; var mol2 = veg[1][1]; var dl2= veg[1][2]; var hl2 = veg[1][3];var ml2= veg[1][4]; var sl2= veg[1][5];
//document.getElementById('de').innerHTML = '2nditem';
var t = new Date(yl2,mol2,dl2,hl2,ml2,sl2).getTime();
var x = setInterval(function() {

    // Get todays date and time
    var now = new Date().getTime();
    //var now = new Date(y1,mo1,d1,h1,m1,s1).getTime();
    // Find the distance between now an the count down date
    var distance = t - now;
    
    // Time calculations for days, hours, minutes and seconds
    //var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    // Output the result in an element with id="demo"
    document.getElementById(lid[1]).innerHTML =  hours + "h "
    + minutes + "m " + seconds + "s ";
    
    // If the count down is over, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById(lid[1]).innerHTML = "EXPIRED";
    }
}, 1000);}
function li3(){
var yl3= veg[2][0]; var mol3 = veg[2][1]; var dl3= veg[2][2]; var hl3 = veg[2][3];var ml3= veg[2][4]; var sl3= veg[2][5];
//document.getElementById('de').innerHTML = '2nditem';
var t = new Date(yl3,mol3,dl3,hl3,ml3,sl3).getTime();
var x = setInterval(function() {

    // Get todays date and time
    var now = new Date().getTime();
    //var now = new Date(y1,mo1,d1,h1,m1,s1).getTime();
    // Find the distance between now an the count down date
    var distance = t - now;
    
    // Time calculations for days, hours, minutes and seconds
    //var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    // Output the result in an element with id="demo"
    document.getElementById(lid[2]).innerHTML =  hours + "h "
    + minutes + "m " + seconds + "s ";
    
    // If the count down is over, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById(lid[2]).innerHTML = "EXPIRED";
    }
}, 1000);}
function li4(){
var yl4= veg[3][0]; var mol4 = veg[3][1]; var dl4= veg[3][2]; var hl4 = veg[3][3];var ml4= veg[3][4]; var sl4= veg[3][5];
//document.getElementById('de').innerHTML = '2nditem';
var t = new Date(yl4,mol4,dl4,hl4,ml4,sl4).getTime();
var x = setInterval(function() {

    // Get todays date and time
    var now = new Date().getTime();
    //var now = new Date(y1,mo1,d1,h1,m1,s1).getTime();
    // Find the distance between now an the count down date
    var distance = t - now;
    
    // Time calculations for days, hours, minutes and seconds
    //var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    // Output the result in an element with id="demo"
    document.getElementById(lid[3]).innerHTML =  hours + "h "
    + minutes + "m " + seconds + "s ";
    
    // If the count down is over, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById(lid[3]).innerHTML = "EXPIRED";
    }
}, 1000);}
