$(document).ready(function() {
	var RouterPrx = Glacier2.RouterPrx;
	var CallbackPrx = Demo.CallbackPrx;
	var CallbackReceiverPrx = Demo.CallbackReceiverPrx;


	function print (data){
		$("#output").val($("#output").val() + data + "\n");
        $("#output").scrollTop($("#output").get(0).scrollHeight);
	} 


	var CallbackReceiverI = Ice.Class(Demo.CallbackReceiver, {
    callback: function(data)
    {
        print(data);
    }
	});
	async function signin(){

		let id = new Ice.InitializationData();
        id.properties = Ice.createProperties();
        //id.properties.setProperty("Ice.Default.Router", router);
        //id.properties.setProperty("Callback.Proxy", "callback:tcp -h localhost -p 10000");
        let communicator = Ice.initialize(id);

        const routerBase = communicator.stringToProxy("DemoGlacier2/router:ws -p 5063 -h localhost");

        const router = await Glacier2.RouterPrx.checkedCast(routerBase);

        communicator.setDefaultRouter(router);

        const base = communicator.stringToProxy("callback:tcp -h localhost -p 10000");

        await router.createSession("userid", "xxx");





        let timeout = await router.getACMTimeout()
        const connection = router.ice_getCachedConnection();
        if(timeout > 0)
        {
            connection.setACM(timeout, undefined, Ice.ACMHeartbeat.HeartbeatAlways);
        }







        const twoway = await Demo.CallbackPrx.checkedCast(base);

        const adapter = await communicator.createObjectAdapterWithRouter("CallbackReceiverAdapter", router);

        await adapter.activate();

        const category = await router.getCategoryForClient();

        const callbackReceiverImpl = new CallbackReceiverI();
		const callbackReceiver = callbackReceiverImpl;

        const callbackReceiverIdent = new Ice.Identity();
        callbackReceiverIdent.name = "callbackReceiver";
		callbackReceiverIdent.category = category;

		const twowayR = CallbackReceiverPrx.uncheckedCast(adapter.add(callbackReceiver, callbackReceiverIdent));

		context = new Ice.Context();
        context.set("_fwd", "t");
        await twoway.initiateCallback(twowayR, context);
        //await twoway.initiateCallback(twowayR, "");
		//await callbackReceiverImpl.callbackOK();


	}

	$('#start').on('click', function(){
      signin()
	});



});