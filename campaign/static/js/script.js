//------------------------------GENERAL DOM MANIPULATION
var totaldays = 0;
var totalcost = 0;

$('#objective_others').hide();
$('#objective').change( ()=>{
    if($('#objective').val()=="Others"){
        $('#objective_others').show();
    }
    else{
        $('#objective_others').hide();
    }
});

$("#professional").change( () => {
    if($('#professional').prop('checked')) {
        $('#procontent').text("YES")
        $('#url').prop( "disabled", true );
        totalcost = parseInt($('#totalcost').val())+300
        $('#totalcost').text(totalcost.toString());
    } else {
        $('#url').prop( "disabled", false );
        $('#procontent').text("NO")
        totalcost = parseInt($('#totalcost').val())-300
        $('#totalcost').text(totalcost.toString());
    }
});



$('.calendar').change( () => {
    if($('#from_date').val() != "" && $('#to_date').val() != "" ){
        

        const startDate = new Date($('#from_date').val())
        const endDate = new Date($('#to_date').val())

        console.log(startDate);
        console.log(endDate);
        
        let diffTime = Math.abs(startDate-endDate)
        let diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        let week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
        let numberOfWeeks = parseInt(diffDays/7)
        let days = new Array(7).fill(numberOfWeeks)
        let initDays = diffDays %7;
        let startDateDay = startDate.getDay();

        days[endDate.getDay()]++;
        for(let i =0;i<initDays;i++){
            days[(i+startDateDay)%7]++;
        }
        let output = {}
        for(let i=0;i<7;i++)
        {
            output[week[i]] = days[i];
            totaldays = totaldays + days[i];
        }
        let weekdays =  days[1] + days[2] + days[3] + days[4]
        let weekend = days[0] + days[5] +days [6]
        var totalcost = weekdays*100 + weekend*150;
        $('#weekdays').text(weekdays.toString())
        $('#weekend_days').text(weekend.toString())

        if($('#professional').prop('checked')) {
            console.log("totalcost",totalcost);
            totalcost = totalcost+300
            $('#totalcost').text(totalcost.toString());
        } else {
            totalcost = totalcost-300
            $('#totalcost').text(totalcost.toString());
        }

    }   
});










// ------------------------GET AND POST METHODS
function AJAXPromise(method, URL) {
    let data = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : null;
    let processData = arguments.length > 3 && arguments[3] !== undefined ? arguments[3] : true;
    let contentType = arguments.length > 4 && arguments[4] !== undefined ? arguments[4] : 'application/x-www-form-urlencoded; charset=UTF-8';

    try {
        return new Promise( (resolve,completed) => {
            try {
                $.ajax({
                    type: method,
                    url: URL,
                    data: data,
                    processData: processData,
                    contentType: contentType,
                    success: function success(data)
                    {
                        resolve(data);
                    },
                    complete: function complete(data)
                    {
                        completed(data);
                    }
                });
            }catch (error) {
                alert(error);
            }
        });
    } catch (error) {
        alert(error);
    }
}



//  ------------------ AUTHENTICATION API'S
$('#signin_submit').click( () => {
    
    let email = $('#signin_email').val();
    let password = $('#signin_password').val();
    
    if (email == undefined || password == undefined){
        window.alert('Enter all credentials!!');
    }
    
    let info = { 'email':email,'password':password }
    var data = { 'data': JSON.stringify(info) };

    
    AJAXPromise("POST", "/signin", data).then( (success_data) => {
        console.log("message:", success_data)
        if ( success_data[0] == 'OK'){
            window.location.replace('/home')
        }
        else {
            console.log("message:", success_data)
            alert('Incorrect Email or Password');
        }
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });
});

$('#signup_submit').click( () => {
    let username = $('#signup_username').val();
    let email =  $('#signup_email').val();
    let password = $('#signup_password').val();
    
    console.log(username,email,password);

    if (username == '' || email == '' || password == ''){
        window.alert('Enter all credentials!!');
    }
    
    let info = { 'username':username, 'email':email, 'password':password }
    var data = { 'data': JSON.stringify(info) };

    console.log(data);

    AJAXPromise("POST", "/verify_email", data).then( (success_data) => {
        if ( success_data.message == 'OK'){
            alert('success');
            window.location.href('/verify_otp')
        }
        else {
            console.log("message:", success_data);
            alert('FAILED');
        }
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });
    
    //AJAXPromise("POST", "/signup", data).then( (success_data) => {
    //    console.log("message:", success_data)
    //    if ( success_data[0] == 'OK'){
    //        alert('');
    //        window.location.replace('/signin')
    //    }
    //    else {
    //        console.log("message:", success_data)
    //        alert('Incorrect Email or Password');
    //    }
    //},(error)=>
    //{
    //  alert(JSON.stringify(error["responseJSON"],null, 1));
    //});
});











//---------------------FUNCTION FOR CREATING NEW CAMPAIGN
$("#campaign_submit").click( ( ) => {
    let mailid   = $('#Email').val();
    let name         =  $('#Name').val();
    let phone        = $('#phone').val();
    let comapnyname     = $('#comapnyname').val();
    let brand      = $('#brand').val();
    let promote      = $('#promote').val();
    let objective    = $('#objective').val();
    let objective_others     = $('#objective_others').val();
    let professional = ''
    if($('input[name="professional"]:checked')){
        professional   = 'yes';
    }else{
        professional = 'no'
    }
    let url     = $('#url').val();
    let start_date = $('#from_date').val()
    let end_date = $('#to_date').val()
    let contenttype = ""

    if (mailid == undefined || name == undefined || phone == undefined ||
        comapnyname == undefined ||
        brand == undefined ||
        promote == undefined ||
        objective == undefined ||
        objective_others == undefined ||
        professional == undefined ||
        start_date == "" || end_date == ""
        ) {
        alert('Please Fill All Details');
    }
    
    let info = { 'name': name,'phone': phone,'email': mailid, 
    'comapnyname' : comapnyname, 'brand': brand,
    'promote': promote, 'objective': objective + objective_others,
    'start_date': start_date,'end_date': end_date, 'total_days':totaldays,
    'professional': professional, 'totalcost':totalcost, 
    'url': url.toString(), 'contenttype': contenttype } ;
    
    //console.log(info);
    
    var data = { 'data': JSON.stringify(info) };
    AJAXPromise("POST", "/new_campaign", data).then( (success_data) => {
        console.log("message:", success_data)

        if ( success_data.message == 'OK'){
            
            alert('success');
        }
        else {
            console.log("message:", success_data)
            alert('DATA ALREADY PRESENT');
        }
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });
    
});












