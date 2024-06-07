document.addEventListener("DOMContentLoaded", function () {
    var videosContainer = document.getElementById("videos");

    // Số lượng video muốn hiển thị
    var numberOfVideos = 7;

    // Tạo và thêm các video vào videosContainer
    for (var i = 0; i < numberOfVideos; i++) {
        var videoContainer = document.createElement("div");
        videoContainer.classList.add("video-container");

        var video = document.createElement("div");
        video.classList.add("video");
        var videoImg = document.createElement("img");
        videoImg.src = "./images/thumbnail" + (i + 1) + ".jpg"; // Đường dẫn đến thumbnail của video
        videoImg.alt = "Video Thumbnail";
        video.appendChild(videoImg);

        var videoInfo = document.createElement("div");
        videoInfo.classList.add("video-info");
        var videoTitle = document.createElement("h3");
        videoTitle.textContent = "Title of the Video Title of the Video Title of the Video" + (i + 1); // Tiêu đề của video
        var channelName = document.createElement("p");
        channelName.textContent = "Channel Name"; // Tên kênh
        var viewsTime = document.createElement("p");
        viewsTime.textContent = "Views • Time ago"; // Lượt xem và thời gian trước
        var videoDescription = document.createElement("p");
        videoDescription.textContent = "Description of the video... Description of the video... Description of the video... Description "; // Mô tả của video

        videoInfo.appendChild(videoTitle);
        videoInfo.appendChild(channelName);
        videoInfo.appendChild(viewsTime);
        videoInfo.appendChild(videoDescription);

        videoContainer.appendChild(video);
        videoContainer.appendChild(videoInfo);

        videosContainer.appendChild(videoContainer);
        console.log("Video", i + 1, "created and added to videosContainer"); // Kiểm tra xem video đã được thêm vào container chưa

    }
});
