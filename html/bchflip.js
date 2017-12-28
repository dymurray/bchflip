window.Bchflip = window.Bchflip || {};
window.Bchflip.Home = window.Bchflip.Home || {};

Bchflip.Home = function Bchflip$Home$Index()
{
	this._coin = $("#coin");
	this._qrModal = $("#qrModal");
	this._GetAddress();
	
}

Bchflip.Home.prototype = 
{
	_sendingAddress: "",
	_receivingAddress: "",
	_coin: {},
	_qrModal: {},
	_bchAvailable: 0,
	
	_BindFunctions: function Bchflip$Bind$Functions()
	{
		$("#flip").click($.proxy(this._FlipCoin, this));
		$("#wager").change($.proxy(this._WagerChange, this));
	},
	
	_GetAddress: function Bchflip$Get$Address()
	{
		//TODO: actually get a new address
		this._receivingAddress = "18f7zXS2RcTAB7VwCemEuSHBBNnfVUPR5m";
		$("#qrModal > .modal-body").innerHTML = "<img src='https://chart.googleapis.com/chart?chs=250x250&cht=qr&chl=%20bitcoincash:" +this._receivingAddress + "?amount=' />";
		this._ShowModal();
		this._BindFunctions();
	},
	
	_ShowModal: function Bchflip$Show$Modal()
	{
		this._qrModal.modal({show: true, backdrop: 'static'});
		timeout = setTimeout($.proxy(this._BCHReceived, this), 5000);
	},
	
	_BCHReceived: function Bchflip$BCH$Received()
	{
		console.log("Modal Hidden");
		this._qrModal.modal('hide');
		this._bchAvailable = 0.5;
		$("#availBCH").text("BCH Available: " + this._bchAvailable);
	},
	
	_FlipCoin: function Bchflip$Flip$Coin()
	{
		var result = Math.floor(Math.random() * 2);
		var userChoice = $(".bf-heads-tails>.active>input").attr("value");
		console.log(userChoice);
		if(result == 0)
		{
		//Got heads
			this._coin.html('<img class="heads animate-coin" src="./heads.png" />');
			
		}
		else
		{
			this._coin.html("<img class='tails animate-coin' src='./tails.png' />");
		}
	},
	
	_WagerChange: function Bchflip$Wager$Change(target)
	{
		var value = parseFloat($(target.currentTarget).val());
		if(value > this._bchAvailable 	)
		{
			$(".bf-user-warning").html("<p class='text-danger text-center'>You can not wager more than you have'</p>");
		}
		else
		{
			$(".bf-user-warning").empty();
			$("#flip").removeAttr("disabled");
		}
	}
}
