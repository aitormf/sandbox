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
    getImageData_async: function(cb, format, current)
    {
        var canvas = document.getElementById("myCanvas");
        //var image = canvas.toDataURL("image/jpeg");
        //image = image.replace("data:image/jpeg;base64,", "")
        let ctx = canvas.getContext('2d');
        let  imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
        let data  = new Uint8Array(imageData.width*imageData.height*3);
        let j = 0;
        for (i=0; i < imageData.data.length; i+=4){
            data[j] = imageData.data[i];
            data[j+1] = imageData.data[i+1];
            data[j+2] = imageData.data[i+2];
            j+=3;
        }
        let msgImage = new jderobot.ImageData();
        let desc = new jderobot.ImageDescription();
        msgImage.pixelData = data;
        desc.width = imageData.width;
        desc.height = imageData.height;
        desc.format = "RGB8";
        msgImage.description = desc;
        cb.ice_response(msgImage);
        return ;
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

        const baseMotors = communicator.stringToProxy("setMotors:ws -h localhost -p 10000");
        const baseCamera = communicator.stringToProxy("setCamera:ws -h localhost -p 10000");

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

        const categoryMotors = await router.getCategoryForClient();
        const motorsImpl = new MotorsI();
		const motors = motorsImpl;
        const motorsIdent = new Ice.Identity();
        motorsIdent.name = "Motors";
        motorsIdent.category = categoryMotors;

        const MotorsR = MotorsPrx.uncheckedCast(adapter.add(motors, motorsIdent));

        contextMotors = new Ice.Context();
        contextMotors.set("_fwd", "t");
        await setterMotors.setMotors(MotorsR, contextMotors);

        console.log("aaaa");
        const cameraImpl = new CameraI();
        const camera = cameraImpl;
        const camerasIdent = new Ice.Identity();
        const categoryCamera = await router.getCategoryForClient();
        camerasIdent.name = "Camera";
        camerasIdent.category = categoryCamera;
        
        const CameraR = CameraPrx.uncheckedCast(adapter.add(camera, camerasIdent));



        contextCamera = new Ice.Context();
        contextCamera.set("_fwd", "t");
        await setterCamera.setCamera(CameraR, contextCamera);


	}

	$('#start').on('click', function(){
      signin()
	});

});