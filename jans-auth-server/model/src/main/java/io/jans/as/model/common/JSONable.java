/*
 * Janssen Project software is available under the Apache License (2004). See http://www.apache.org/licenses/ for full text.
 *
 * Copyright (c) 2020, Janssen Project
 */

package io.jans.as.model.common;

import org.json.JSONException;
import org.json.JSONObject;

/**
 * @author Javier Rojas Blum Date: 13.01.2013
 */
public interface JSONable {

    JSONObject toJSONObject() throws JSONException;
}