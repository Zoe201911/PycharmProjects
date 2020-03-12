import requests
import json
import urllib3
urllib3.disable_warnings()

def bky_login():
    '''登陆博客园，并且带着登陆的cookies'''
    s = requests.session()
    # 全局设置
    s.verify = False

    # 更新s里面的cookies
    c = requests.cookies.RequestsCookieJar()
    c.set(".CNBlogsCookie",
          "F238F3ABEDDB276EED97427BCEAEFD037E7E53644CF6C9C7642BA6235FABBBA0FDBDF5F3F027425040CB5E57CD8EF5A80B8DA1631C21F1EBC8FB79F5A9CE5C9F5AAB63E8A8069D202056501C9824C68112317F02")
    c.set(".Cnblogs.AspNetCore.Cookies",
          "CfDJ8D8Q4oM3DPZMgpKI1MnYlrm_OBJilc536S7iWVczH_Uq0QejmIYlGF3-ItaQyB5vlPNH51N78WvKJsdBxhcegpjSErm2yOW6qtXXrEtd0SoHc1_rUHbbUaghmKOoJuO6jIVPfV5noYzo7ARNtGWLJ2e4ib9AJ-0EZSR6tpiSn_UAW99U1JmFKyTKt8Dk0LiG9tY4e1pdSikgvztSLmM-amumC3HRhHuB9guf690guwJgl97xRnlJ0pzw7C2AMZUxSvUKsOvOD3xN261NU_TvvQ0V9HsxhPx7zz9GyGjXRlJ5gRFfdGP6E5kl1ktXRApmOg")
    s.cookies.update(c)

    url = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
    r = s.get(url)

if __name__ == '__main__':
    bky_login()