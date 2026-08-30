#7. Write a program to find out whether a given post is talking about “Harry” or not.

post = "'hey Harry ', all good brother!"

if ( "Harry".lower() in post.lower()):
    print('This Post is talking about harry')
else:
    print('this post isnot talking about harry')