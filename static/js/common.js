$(".eqSelector").click(function(){
	$("#eqSelectorGroup > button").html($(this).html()+"<span class=\"caret\"></span>");
	$(this).parent().siblings().removeClass("active");
	$(this).parent().addClass("active");
	$.ajax({
		url:"/getCpSelector/"+$(this).attr("eqID"),
		type:"get",
		beforeSend:function(){
			$("#loadingPanel").fadeIn("fast");
		},
		success:function(result){
			if($("#cpSelectorGroup").length>0){
				$("#cpSelectorGroup").remove();
			};
			$("#eqSelectorGroup").after(result);
		},
		complete:function(){
			$("#loadingPanel").fadeOut("fast");
		}
	});
});