$(document).ready(function() {
	var RouterPrx = Glacier2.RouterPrx;
    var SetterMotorsPrx = jderobot.SetterMotorsPrx;
	var SetterCameraPrx = jderobot.SetterCameraPrx;
    var MotorsPrx = jderobot.MotorsPrx;
	var CameraPrx = jderobot.CameraPrx;


	function print (data){
		$("#output").val($("#output").val() + data + "\n");
        $("#output").scrollTop($("#output").get(0).scrollHeight);
	} 


	var CameraI = Ice.Class(jderobot.Camera, {
    setCameraDescription: function(data)
    {
        print("setCameraDescription: "+ data);
        return 1;
    }, 
    getCameraDescription: function()
    {
        return new jderobot.CameraDescription();
    },
    startCameraStreaming: function()
    {
        return "1";
    },
    stopCameraStreaming: function()
    {
        return 1;
    },
    reset: function()
    {
        return 1;
    },
    getImageDescription: function()
    {
        return new jderobot.ImageDescription();
    },
    getImageFormat: function()
    {
        return new jderobot.ImageFormat();
    },
    getImageData: function(format)
    {
        canvas = document.getElementById("myCanvas");
        image = canvas.toDataURL("image/jpeg");
        image = image.replace("data:image/jdpeg;base64,", "")
        msgImage = new jderobot.ImageData();
        msgImage.pixelData = image
        msgIMage.description.width = 300;
        msgIMage.description.height = 150;
        msgIMage.description.format = "jpeg";
        return msgIMage;
    }
	});




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

        const baseMotors = communicator.stringToProxy("setMotors:tcp -h localhost -p 10000");
        const baseCamera = communicator.stringToProxy("setCamera:tcp -h localhost -p 10000");

        await router.createSession("userid", "xxx");



        let timeout = await router.getACMTimeout()
        const connection = router.ice_getCachedConnection();
        if(timeout > 0)
        {
            connection.setACM(timeout, undefined, Ice.ACMHeartbeat.HeartbeatAlways);
        }




        const setterMotors = await jderobot.SetterMotorsPrx.checkedCast(baseMotors);
        const setterCamera = await jderobot.SetterCameraPrx.checkedCast(baseCamera);
        const adapter = await communicator.createObjectAdapterWithRouter("Adapter", router);

        await adapter.activate();

        const category = await router.getCategoryForClient();
        const motorsImpl = new MotorsI();
        const cameraImpl = new CameraI();
		const motors = motorsImpl;
        const camera = cameraImpl;

        const motorsIdent = new Ice.Identity();
        const camerasIdent = new Ice.Identity();

        motorsIdent.name = "Motors";
        motorsIdent.category = category;

        camerasIdent.name = "Camera";
        camerasIdent.category = category;

		const MotorsR = MotorsPrx.uncheckedCast(adapter.add(motors, motorsIdent));
        const CameraR = CameraPrx.uncheckedCast(adapter.add(camera, camerasIdent));



        contextCamera = new Ice.Context();
        contextCamera.set("_fwd", "t");
        await setterCamera.setCamera(CameraR, contextCamera);

		contextMotors = new Ice.Context();
        contextMotors.set("_fwd", "t");
        await setterMotors.setMotors(MotorsR, contextMotors);
        //await twoway.initiateCallback(twowayR, "");
		//await motorsImpl.callbackOK();


	}

	$('#start').on('click', function(){
      signin()
	});

});