$(document).ready(function() {
	var RouterPrx = Glacier2.RouterPrx;
	var SetterMotorsPrx = jderobot.SetterMotorsPrx;
	var MotorsPrx = jderobot.MotorsPrx;


	function print (data){
		$("#output").val($("#output").val() + data + "\n");
        $("#output").scrollTop($("#output").get(0).scrollHeight);
	} 


	var MotorsI = Ice.Class(jderobot.Motors, {
    setV: function(data)
    {
        print("v: "+ data);
    },
    setW: function(data)
    {
        print("w: "+ data);
    },
    setL: function(data)
    {
        print("l: "+ data);
    },
    getV: function()
    {
        return 1;
    },
    getW: function()
    {
        return 1;
    },
    getL: function()
    {
        return 1;
    }
	});
    
	async function signin(){

		let id = new Ice.InitializationData();
        id.properties = Ice.createProperties();
        let communicator = Ice.initialize(id);

        const routerBase = communicator.stringToProxy("DemoGlacier2/router:ws -p 5063 -h localhost");

        const router = await Glacier2.RouterPrx.checkedCast(routerBase);

        communicator.setDefaultRouter(router);

        const base = communicator.stringToProxy("setMotors:tcp -h localhost -p 10000");

        await router.createSession("userid", "xxx");





        let timeout = await router.getACMTimeout()
        const connection = router.ice_getCachedConnection();
        if(timeout > 0)
        {
            connection.setACM(timeout, undefined, Ice.ACMHeartbeat.HeartbeatAlways);
        }







        const twoway = await jderobot.SetterMotorsPrx.checkedCast(base);

        const adapter = await communicator.createObjectAdapterWithRouter("MotorsAdapter", router);

        await adapter.activate();

        const category = await router.getCategoryForClient();

        const motorsImpl = new MotorsI();
		const motors = motorsImpl;

        const motorsIdent = new Ice.Identity();
        motorsIdent.name = "Motors";
		motorsIdent.category = category;

		const twowayR = MotorsPrx.uncheckedCast(adapter.add(motors, motorsIdent));

		context = new Ice.Context();
        context.set("_fwd", "t");
        await twoway.setMotors(twowayR, context);
        //await twoway.initiateCallback(twowayR, "");
		//await motorsImpl.callbackOK();


	}

	$('#start').on('click', function(){
      signin()
	});



});