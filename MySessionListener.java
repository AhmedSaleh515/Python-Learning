package com.atguigu.listeners;

import jakarta.servlet.annotation.WebListener;
import jakarta.servlet.http.*;

@WebListener
public class MySessionListener implements HttpSessionListener, HttpSessionAttributeListener {

    @Override
    public void sessionCreated(HttpSessionEvent se) {
        HttpSession session = se.getSession();
        System.out.println("Session " + session.getId() + " created.");
    }

    @Override
    public void sessionDestroyed(HttpSessionEvent se) {
        HttpSession session = se.getSession();
        System.out.println("Session " + session.getId() + " destroyed (invalidated).");
    }

    @Override
    public void attributeAdded(HttpSessionBindingEvent se) {
        System.out.println("Session attribute added: " + se.getName() + " = " + se.getValue());
    }

    @Override
    public void attributeRemoved(HttpSessionBindingEvent se) {
        System.out.println("Session attribute removed: " + se.getName());
    }

    @Override
    public void attributeReplaced(HttpSessionBindingEvent se) {
        String name = se.getName();
        Object oldValue = se.getValue();
        Object newValue = se.getSession().getAttribute(name);
        System.out.println("Session attribute changed: " + name + " from " + oldValue + " to " + newValue);
    }
}