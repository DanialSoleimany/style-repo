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

# In[4]:


cards = """
<style>
.card-container {
    display: flex;
    justify-content: space-between;
    margin: 0px 0;
}

.card {
    width: 320px;  /* Adjust the width as needed */
    height: 250px;  /* Half of the original height */
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

# In[7]:


titles = """
<style>
.text-gradient-hover {
    font-size: 18px;
    padding: 0px;  
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


# In[101]:


title_steps = """
<style>
  .hover-effect {
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
  }

  .hover-effect .overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to right, rgb(139, 48, 88), rgb(173, 70, 108));
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .hover-effect:hover .overlay {
    opacity: 1;
  }

  .hover-effect:hover .text {
    color: rgb(255, 198, 196);
  }

  .text {
    padding: 5px;
    position: relative;
    z-index: 1;
    transition: color 0.3s ease; 
    color: rgb(139, 48, 88);
    text-align:center;
    font-family:cursive;
    font-size: 28px;
  }
</style>
"""

# %store title_steps


# In[26]:


steps = """
<style>
  .hover-steps {
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    background-color: rgb(255, 198, 196); /* Set the custom background color here */
    border-radius:10px
  }

  .hover-steps .overlay-steps {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(to right, rgb(173, 70, 108), rgb(173, 70, 108));
    opacity: 0;
    transition: opacity 0.3s ease;
  }

  .hover-steps:hover .overlay-steps {
    opacity: 1;
  }

  .hover-steps:hover .text-steps {
    color: rgb(255, 198, 196);
  }

  .text-steps {
    padding: 15px;
    position: relative;
    z-index: 1;
    font-size: 24px;
    transition: color 0.3s ease; 
    color: rgb(139, 48, 88);
    text-align: center;
  }
</style>
"""

# %store steps


# In[126]:


move_table = """
<style>
    .three-d-shape {
        position: relative;
        width: 250px;
        height: 30px;
        background: linear-gradient(to right, rgb(103, 32, 68), rgb(173, 70, 108));
        border-radius: 10px;
        box-shadow: 1px 1px 1px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        overflow: hidden;
        float: right; /* Add this property to move it to the right */
    }
    .three-d-text {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        color: white;
        font-size: 12px;
        font-weight: bold;
    }
    .three-d-shape:hover {
        transform: translate(5px, 5px);
        box-shadow: 2px 2px 3px rgba(0, 0, 0, 0.3);
    }
</style>
"""

# %store move_table


# In[23]:


visual_steps = """
<style>
  .visual-steps {
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    background: linear-gradient(to right, rgb(255, 198, 196), rgb(255, 198, 196));
    border-radius: 10px;
    transition: background 0.7s ease;
  }

  .visual-steps:hover {
    background: linear-gradient(to right, rgb(255, 198, 196), rgb(255, 198, 196));
  }

  .visual-steps .overlay-visual-steps {
    position: absolute;
    top: 0;
    left: -100%; /* Initial position off-screen to the left */
    width: 100%;
    height: 100%;
    background: linear-gradient(to right, rgb(173, 70, 108), rgb(173, 70, 108));
    opacity: 0;
    transition: left 0.7s ease, opacity 0.7s ease;
  }

  .visual-steps:hover .overlay-visual-steps {
    left: 0; /* Move to the original position on hover */
    opacity: 1;
  }

  .visual-steps:hover .text-visual-steps {
    color: rgb(255, 198, 196);
  }

  .text-visual-steps {
    padding: 5px;
    position: relative;
    z-index: 1;
    font-size: 18px;
    transition: color 0.3s ease; 
    color: rgb(139, 48, 88);
    text-align: center;
  }
</style>

"""

# %store visual_steps


# In[ ]:




