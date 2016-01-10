var handleFiles = function(files) {
	var imageHolder = document.getElementById('image-holder');

	// clear image holder
	while (imageHolder.firstChild) {
		imageHolder.removeChild(imageHolder.firstChild);
	}

	for (var i = 0; i < files.length; i++) {
		var file = files[i];

		// if it's not an image, ignore it
		if (!/^image\//.test(file.type)) {
			return;
		}

		var img = document.createElement('img');
		img.classList.add('image-preview');
		img.file = file;
		imageHolder.appendChild(img);
		imageHolder.appendChild(document.createElement('br'));
		if (i < files.length - 1) {
			imageHolder.appendChild(document.createElement('br'));
		}

		var reader = new FileReader();
		reader.onload = (function(image) {
			return function(e) {
				image.src = e.target.result;
			};
		})(img);
		reader.readAsDataURL(file);
	}
}
