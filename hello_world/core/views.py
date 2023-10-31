from django.shortcuts import render

def index(request):
    context = {
        "title": "Ablog",
    }
    return render(request, "ablog/index.html", context)

def blog_post(request):
    context = {}
    return render(request, "ablog/blog-post.html", context=context)

def profile(request):
    context = {}
    return render(request, "ablog/profile.html", context=context)

def blogDetail(request,blogid):

    dataObj = { 
        "coverImage" : "https://t3.ftcdn.net/jpg/05/91/97/64/360_F_591976463_KMZyV6obpsrN2bJJJkYW0bzoH2XxLTlA.jpg",
        "topic" : "This is topic",
        "date" : "11/12/2023",
        "content" : '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. A diam maecenas sed enim ut sem viverra. Eu facilisis sed odio morbi quis commodo odio. Dui sapien eget mi proin sed libero enim sed faucibus. Mattis rhoncus urna neque viverra justo nec ultrices dui sapien. Habitant morbi tristique senectus et netus. Gravida quis blandit turpis cursus. Felis donec et odio pellentesque. Orci phasellus egestas tellus rutrum tellus. Praesent elementum facilisis leo vel. Est pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat vivamus.

Nunc congue nisi vitae suscipit tellus mauris. Amet volutpat consequat mauris nunc congue nisi vitae suscipit tellus. Viverra tellus in hac habitasse. In metus vulputate eu scelerisque felis imperdiet proin fermentum. Fusce id velit ut tortor pretium viverra suspendisse potenti nullam. Dolor morbi non arcu risus quis. Fringilla urna porttitor rhoncus dolor purus. Consectetur adipiscing elit pellentesque habitant. Arcu bibendum at varius vel pharetra vel turpis nunc eget. Eleifend mi in nulla posuere sollicitudin. Nascetur ridiculus mus mauris vitae ultricies leo integer malesuada. Vitae proin sagittis nisl rhoncus. Sit amet facilisis magna etiam tempor orci eu lobortis elementum. Volutpat ac tincidunt vitae semper quis lectus. Enim sit amet venenatis urna. Lorem ipsum dolor sit amet consectetur adipiscing. At augue eget arcu dictum varius duis at consectetur lorem. Amet est placerat in egestas erat imperdiet sed. Elementum curabitur vitae nunc sed velit dignissim. Lorem dolor sed viverra ipsum nunc aliquet bibendum enim facilisis.''', 
    }

    context = {
        "title" : "BlogDetail",
        "id": blogid,
        "data": dataObj
    }
    return render(request, "ablog/detail.html", context=context)

