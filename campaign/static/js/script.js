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
        $('#url').prop( "disabled", true );
    } else {
        $('#url').prop( "disabled", false );
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
        totalcost = weekdays*100 + weekend*150;
        
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


//FUNCTION FOR CREATING NEW CAMPAIGN
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
    
    console.log(info);
    
    var data = { 'data': JSON.stringify(info) };
    AJAXPromise("POST", "/new_campaign", data).then( (success_data) => {
        if ( success_data.message == 'ok'){
            alert('success');
        }
        else {
            alert('DATA ALREADY PRESENT');
        }
    },(error)=>
    {
      alert(JSON.stringify(error["responseJSON"],null, 1));
    });
    
});












