#!/usr/bin/env python
# coding: utf-8

# ### Table of Contents Style

# In[1]:


table_contents = """<style>
.hover-effect-container {
    position: relative;
    display: inline-block;
  }

  .hover-effect-text {
    display: inline-block;
    position: relative;
    z-index: 1;
    font-size: 20px;
    transition: color 0.3s ease;
    padding: 15px;
    color: rgb(103, 32, 68);
  }

  .hover-effect-background {
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 100%;
    background: linear-gradient(to right, rgb(173, 70, 108), rgb(204, 96, 125));
    transition: right 0.3s ease, height 0.3s ease;
    border-radius: 15px;
  }

  .hover-effect-container:hover .hover-effect-background {
    right: 0;
    border-radius: 10px;
  }

  .hover-effect-container:hover .hover-effect-text {
    color: rgb(255, 198, 196);
  }
</style>"""

# %store table_contents


# ### Cards Style

# In[2]:


cards = """
<style>
.card-container {
    display: flex;
    justify-content: space-between;
    margin: 0px 0;
}

.card {
    width: 320px;  /* Adjust the width as needed */
    height: 300px;
    background-color: rgb(139, 48, 88);
    border: 1px solid ccc;
    border-radius: 8px;
    overflow: hidden;
    position: relative;
    transition: background-color 0.5s ease;
}

.card:hover {
    background-color: rgb(103, 32, 68);
}

.card-content {
    padding: 20px;
    color: rgb(255, 198, 196);
}

.title {
    color: rgb(227, 129, 145);
}
</style>
"""

# %store cards


# ### Titles Style

# In[3]:


titles = """
<style>
.text-gradient-hover {
    font-size: 18px;
    padding: 30px;  
    background: linear-gradient(to right, rgb(173, 70, 108), rgb(227, 129, 145));
    color: rgb(255, 198, 196);
    transition: background-position 0.3s ease-in-out, color 0.5s ease;  /* Specify the transition duration for color */
    background-size: 200% 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%; /* Ensure the element takes the full height of its container */
}

.text-gradient-hover:hover {
    background-position: right center;
    color: rgb(103, 32, 68);
}

.text-gradient-hover h2 {
    padding: 0px;  /* Adjust the outer padding as needed */
    margin: 10;  /* Remove default margin to ensure the padding is consistent */
}
</style>
"""

# %store titles


# ### Question Style

# In[4]:


question = """
<style>
  .hover-effect {
    background-color: rgb(255, 220, 196);
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s ease;
  }

  .hover-effect:hover {
    background-color: #ffd2ae;
  }

  .text {
  padding: 20px;
    font-size: 22px;
    font-family: 'Arial', Times, serif;
    line-height: 1.6em;
    text-align: center;
    color: #333;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
  }
</style>
"""

# %store question


# In[ ]:




