import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../hooks/useAuth";
import {
  Dialog,
  Button,
  Text,
  Heading,
  TextField,
  Flex,
} from "@radix-ui/themes";

const LoginModal = ({ visible, setVisible, mode }) => {
  const navigate = useNavigate();
  const { login, register, loading, error } = useAuth();
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");

  const handleRegister = async () => {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    if (!regex.test(email)) {
      alert("Not a valid email format");
      return;
    }

    try {
      await register(email, userName, password);
      navigate("/home");
      setVisible(false);
    } catch (e) {
      if (e.status === 409) {
        alert("Username already exists");
      } else {
        alert("Error while trying to register");
      }
    }
  };

  const handleLogin = async () => {
    try {
      await login(userName, password);
      navigate("/home");
      setVisible(false);
    } catch (e) {
      console.error(e.message);
    }
  };

  return (
    <Dialog.Root open={visible} onOpenChange={setVisible}>
      <Dialog.Content maxWidth="400px">
        <Dialog.Title></Dialog.Title>
        {mode === "login" ? (
          <Flex direction="column" gap="3">
            <Heading size="7">Log in</Heading>

            <Text>User Name</Text>
            <TextField.Root
              value={userName}
              placeholder="Username"
              onChange={(e) => setUserName(e.target.value)}
            />

            <Text>Password</Text>
            <TextField.Root
              value={password}
              type="password"
              placeholder="Password"
              onChange={(e) => setPassword(e.target.value)}
            />

            {error && (
              <Text size="22" style={{ marginTop: "5px" }}>
                {error}
              </Text>
            )}
            <Button
              disabled={loading}
              onClick={() => {
                handleLogin();
              }}
            >
              Login
            </Button>
          </Flex>
        ) : (
          <Flex direction="column" gap="3">
            <Heading size="7">Register</Heading>

            <Text>Email</Text>

            <TextField.Root
              value={email}
              type="email"
              placeholder="Email"
              onChange={(e) => setEmail(e.target.value)}
            />

            <Text>User Name</Text>

            <TextField.Root
              value={userName}
              placeholder="Username"
              onChange={(e) => setUserName(e.target.value)}
            />

            <Text>Password</Text>

            <TextField.Root
              value={password}
              type="password"
              placeholder="Password"
              onChange={(e) => setPassword(e.target.value)}
            />
            <Button onClick={handleRegister} disabled={loading}>
              Register
            </Button>
          </Flex>
        )}
      </Dialog.Content>
    </Dialog.Root>
  );
};

export default LoginModal;
