const sortSelector = document.getElementById("sort-selector");

if (sortSelector) {
    sortSelector.addEventListener("change", function () {
        const currentUrl = new URL(window.location);
        const selectedValue = sortSelector.value;

        if (selectedValue === "reset") {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");
        } else {
            const parts = selectedValue.split("_");
            currentUrl.searchParams.set("sort", parts[0]);
            currentUrl.searchParams.set("direction", parts[1]);
        }

        window.location.replace(currentUrl);
    });
}
