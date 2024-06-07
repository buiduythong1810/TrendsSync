document.addEventListener("DOMContentLoaded", function () {
    var trendingData = [
        "U23 Indonesia đấu với U23 Guinea",
        "Hoàng Anh Gia Lai đấu với Sông Lam Nghệ An",
        "Hà Nội đấu với Viettel",
        "Tiêm vaccine Covid-19",
        "Europa League",
        "Nguyễn Văn Bình, Vụ trưởng Vụ Pháp chế",
        "Quy hoạch mở rộng đường Láng",
        "Xe điện VinFast vf3",
        "Cách nấu cơm",
        "Xem phim online",
        "Dự báo thời tiết",
        "Cách làm bún chả",
        "'Trend' cực hot nhưng không phải ai đu cũng được",
        "Chủ mì tôm thanh long nói về nghi vấn dùng chiêu trò marketing",
        "Trà chanh giã tay lên trend, khách mua phải xếp hàng lấy số"
        // Thêm các dữ liệu trending khác nếu cần
    ];

    var trendList = document.getElementById("trend-list");
    trendingData.forEach(function (trend, index) {
        var listItem = document.createElement("li");
        listItem.classList.add("trend-item");

        var trendIndex = document.createElement("div");
        trendIndex.classList.add("trend-index");
        trendIndex.textContent = index + 1;

        var trendContent = document.createElement("div");
        trendContent.classList.add("trend-content");
        trendContent.textContent = trend;

        listItem.appendChild(trendIndex);
        listItem.appendChild(trendContent);

        trendList.appendChild(listItem);
    });
});
